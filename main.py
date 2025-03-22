#!/usr/bin/env python3
"""
LLM-Tools Server - Providing tools to LLMs through Model Context Protocol (MCP)
"""

import logging
from typing import Optional

from mcp.server.fastmcp import FastMCP

from src.tools.duckduckgo import DuckDuckGoTool

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("llm-tools")


def main(port: int = 8000) -> None:
    """
    Initialize and start the MCP server with all available tools.

    Args:
        port: The port number to run the server on (default: 8000)
    """

    # Create an MCP server
    mcp = FastMCP(name="Demo", port=port)

    """Register all available tools with the MCP server."""
    # Create tool instances
    duckduckgo_tool = DuckDuckGoTool()

    @mcp.tool()
    def web_search(query: str, num_results: Optional[int] = 5) -> list:
        """
        Search the web for information on a given query.

        Provide a detailed query for the best results, including keywords, locations, etc.

        Args:
            query: A detailed search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """
        return duckduckgo_tool.web_search(query=query, num_results=num_results)

    @mcp.tool()
    def news_search(query: str, num_results: Optional[int] = 5) -> list:
        """
        Search the web for news on a given query.

        Provide a detailed query for the best results, including keywords, locations, etc.

        Args:
            query: A detailed search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """
        return duckduckgo_tool.news_search(query=query, num_results=num_results)

    @mcp.tool()
    def image_search(query: str, num_results: Optional[int] = 5) -> list:
        """
        Search the web for images for the given query.

        Provide a detailed query for the best results, including keywords, locations, etc.

        Args:
            query: A detailed search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """
        return duckduckgo_tool.image_search(query=query, num_results=num_results)

    @mcp.tool()
    def video_search(query: str, num_results: Optional[int] = 5) -> list:
        """
        Search the web for videos for the given query.

        Provide a detailed query for the best results, including keywords, locations, etc.

        Args:
            query: A detailed search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """
        return duckduckgo_tool.video_search(query=query, num_results=num_results)

    # Add an addition tool
    # @mcp.tool()
    # def add(a: int, b: int) -> int:
    #     """Add two numbers"""
    #     return a + b

    # Add a dynamic greeting resource
    @mcp.resource("greeting://{name}")
    def get_greeting(name: str) -> str:
        """Get a personalized greeting"""
        return f"Hello, {name}!"

    logger.info(f"Starting MCP server on port {mcp.settings.port} ...")
    logger.info(f"Settings {mcp.settings}")

    mcp.run(transport="sse")

    logger.info("MCP server stopped.")


if __name__ == "__main__":
    import argparse

    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description='LLM-Tools Server - MCP protocol server providing tool access to LLMs')

    parser.add_argument('--port', type=int, default=8001,
                        help='Port to run the server on (default: 8001)')

    args = parser.parse_args()

    # Run the server with the specified port
    main(port=args.port)
