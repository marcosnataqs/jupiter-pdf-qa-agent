"""LangGraph ReAct agent implementation for PDF QA."""

from typing import Annotated, Literal, TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from src.tools import get_available_tools


class AgentState(TypedDict):
    """State of the agent graph."""
    
    messages: Annotated[list, add_messages]


class PDFQAAgent:
    """ReAct-style agent for PDF question answering."""
    
    def __init__(self):
        """Initialize the agent."""
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        
        # Get available tools
        self.tools = get_available_tools()
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        
        # Build the agent graph
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph agent workflow.
        
        Returns:
            Compiled graph ready for execution
        """
        workflow = StateGraph(AgentState)
        
        # Define nodes
        workflow.add_node("agent", self._call_agent)
        workflow.add_node("tools", ToolNode(self.tools))
        
        # Set entry point
        workflow.set_entry_point("agent")
        
        # Add conditional edges
        workflow.add_conditional_edges(
            "agent",
            self._should_continue,
            {
                "continue": "tools",
                "end": END,
            }
        )
        
        # After tools, return to agent
        workflow.add_edge("tools", "agent")
        
        return workflow.compile()
    
    def _call_agent(self, state: AgentState) -> dict:
        """Call the LLM with current state and tools.
        
        Args:
            state: Current agent state
            
        Returns:
            Updated state with agent response
        """
        messages = state["messages"]
        
        # Add system message
        system_msg = SystemMessage(
            content=(
                "You are a helpful assistant that answers questions about uploaded PDF documents. "
                "Use the retrieval tool to find relevant information from the documents. "
                "Always cite your sources using the format: (filename.pdf p.X) when answering. "
                "If you don't have enough information, say so clearly."
            )
        )
        
        # Combine system message with conversation messages
        full_messages = [system_msg] + messages
        
        response = self.llm_with_tools.invoke(full_messages)
        return {"messages": [response]}
    
    def _should_continue(self, state: AgentState) -> Literal["continue", "end"]:
        """Determine if the agent should continue with tool calls or end.
        
        Args:
            state: Current agent state
            
        Returns:
            "continue" if there are tool calls to make, "end" otherwise
        """
        last_message = state["messages"][-1]
        
        # If there are tool calls, continue
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "continue"
        
        return "end"
    
    def run(self, user_message: str) -> str:
        """Run the agent with a user message.
        
        Args:
            user_message: The user's question
            
        Returns:
            The agent's response
        """
        # Create message
        message = HumanMessage(content=user_message)
        
        # Invoke the graph
        result = self.graph.invoke({
            "messages": [message],
        })
        
        # Extract final response
        final_message = result["messages"][-1]
        response_text = final_message.content
        
        return response_text