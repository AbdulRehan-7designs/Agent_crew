# tools.py
# PURPOSE: Helper functions for external data gathering

from duckduckgo_search import DDGS

def perform_web_search(query: str) -> list[dict]:
    """
    Search the web for current information.
    Returns a list of result dictionaries.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5, backend='html'))
        return results
    except Exception as e:
        print(f"Search failed: {e}")
        return []

def format_search_results(results: list[dict]) -> str:
    """Formats the raw search results into a string for the LLM context."""
    if not results:
        return "No results found."
        
    formatted = []
    for i, r in enumerate(results, 1):
        formatted.append(
            f"Result {i}:\n"
            f"Title: {r.get('title', 'N/A')}\n"
            f"Summary: {r.get('body', 'N/A')}\n"
            f"URL: {r.get('href', 'N/A')}\n"
        )
    return "\n---\n".join(formatted)