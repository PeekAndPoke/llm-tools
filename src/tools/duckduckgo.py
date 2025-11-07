"""
Web search tool for LLM integration using MCP protocol.
Provides search capabilities to query the web for information.
"""
from ddgs import DDGS


class DuckDuckGoTool:
    """Tool for performing web searches and retrieving results."""

    # https://pypi.org/project/duckduckgo-search/

    def __init__(self):
        self.ddgs = DDGS()

    def web_search(self, query: str, num_results: int = 5) -> str | list[dict[str, str]]:
        """
        Perform a web search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        try:
            result = self.ddgs.text(query=query,
                                    max_results=num_results)

            return result

        except Exception as e:
            return "Error: " + str(e)

    def news_search(self, query: str, num_results: int = 5) -> str | list[dict[str, str]]:
        """
        Perform a web search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        try:
            result = self.ddgs.news(query=query,
                                    max_results=num_results)

            return result

        except Exception as e:
            return "Error: " + str(e)

    def image_search(self, query: str, num_results: int = 5) -> str | list[dict[str, str]]:
        """
        Perform an image search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        try:
            result = self.ddgs.images(query=query,
                                      max_results=num_results)

            return result

        except Exception as e:
            return "Error: " + str(e)

    def video_search(self, query: str, num_results: int = 5) -> str | list[dict[str, str]]:
        """
        Perform a video search for the given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """

        try:
            result = self.ddgs.videos(query=query,
                                      max_results=num_results)

            return result

        except Exception as e:
            return "Error: " + str(e)
