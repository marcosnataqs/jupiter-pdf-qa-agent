"""Tool registry for the PDF QA agent."""

from typing import List
from langchain_core.tools import tool


@tool
def retrieve_pdf_chunks(query: str, top_k: int = 5) -> str:
    """Retrieve relevant chunks from uploaded PDF documents.

    This is a PLACEHOLDER. During the live coding session, implement:
    - Store uploaded PDFs and their chunks
    - Search through chunks using the query
    - Return top-k most relevant chunks with citations

    Args:
        query: The search query or question
        top_k: Number of top results to return (default: 5)

    Returns:
        A formatted string with retrieved chunks and citations
    """
    # TODO: Implement during live coding session
    return "No PDF retrieval implemented yet. TODO: Implement document storage and retrieval logic."


def get_available_tools() -> List:
    """Get the list of tools available to the agent.

    Returns:
        List of LangChain tools
    """
    return [retrieve_pdf_chunks]
