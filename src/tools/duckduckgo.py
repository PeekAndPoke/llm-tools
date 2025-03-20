"""
Web search tool for LLM integration using MCP protocol.
Provides search capabilities to query the web for information.
"""

from typing import Dict, Any, List

from duckduckgo_search import DDGS


class DuckDuckGoTool:
    """Tool for performing web searches and retrieving results."""

    # https://pypi.org/project/duckduckgo-search/

    def __init__(self):
        self.ddgs = DDGS()

    def web_search(
            self,
            query: str,
            num_results: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Perform a web search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        result = self.ddgs.text(keywords=query,
                                max_results=num_results)

        return result

    def news_search(
            self,
            query: str,
            num_results: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Perform a web search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        result = self.ddgs.news(keywords=query,
                                max_results=num_results)

        return result

    def image_search(
            self,
            query: str,
            num_results: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Perform an image search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        result = self.ddgs.images(keywords=query,
                                  max_results=num_results)

        return result

    def video_search(
            self,
            query: str,
            num_results: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Perform a video search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        result = self.ddgs.videos(keywords=query,
                                  max_results=num_results)

        return result
