#!/usr/bin/env python3
"""
LLM-Tools Server - Providing tools to LLMs through Model Context Protocol (MCP)
"""

import logging
from datetime import datetime
from typing import Optional

from mcp.server.fastmcp import FastMCP

from src.tools.duckduckgo import DuckDuckGoTool
from src.tools.eventsearch import EventSearchTool
from src.tools.weather import WeatherTool

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
    mcp = FastMCP(name="Demo",
                  # port=port,
                  debug=True)

    """Register all available tools with the MCP server."""
    # Create tool instances
    weather_tool = WeatherTool()
    duckduckgo_tool = DuckDuckGoTool()
    events_tool = EventSearchTool()

    # FastMCP requires functions, so we'll create wrapper functions for our tools
    @mcp.tool()
    def weather_forecast(location: str) -> dict:
        """Get weather forecast for a specific location."""
        return weather_tool._run(location)

    @mcp.tool()
    def web_search(query: str, num_results: Optional[int] = 5) -> list:
        """
        Search the web for information on a given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """
        return duckduckgo_tool.web_search(query=query, num_results=num_results)

    @mcp.tool()
    def news_search(query: str, num_results: Optional[int] = 5) -> list:
        """
        Search the web for news on a given query.

        Args:
            query: The search query string
            num_results: Number of results to return (default: 5)

        Returns:
            List of search results, each containing title, snippet, and URL
        """
        return duckduckgo_tool.news_search(query=query, num_results=num_results)

    @mcp.tool()
    async def event_search(city: str,
                           from_date: Optional[datetime] = None,
                           to_date: Optional[datetime] = None,
                           query: Optional[str] = None) -> str:
        """
        Search for upcoming events in the given city.
        :param city: The city to search for events in
        :param from_date: The start date of the search (default: today)
        :param to_date: The end date of the search (default: today)
        :param query: An additional search filter
        :return: Found content as markdown
        """
        return await events_tool.search(city=city, from_date=from_date, to_date=to_date, query=query)

    # Add an addition tool
    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    # Add a dynamic greeting resource
    @mcp.resource("greeting://{name}")
    def get_greeting(name: str) -> str:
        """Get a personalized greeting"""
        return f"Hello, {name}!"

    logger.info(f"Starting MCP server on port {port} ...")
    # mcp.run(transport="sse")
    mcp.run(transport="sse")
    logger.info("MCP server stopped.")


if __name__ == "__main__":
    import argparse

    # Set up command line argument parsing
    parser = argparse.ArgumentParser(
        description='LLM-Tools Server - MCP protocol server providing tool access to LLMs')

    parser.add_argument('--port', type=int, default=8000,
                        help='Port to run the server on (default: 8001)')

    args = parser.parse_args()

    # Run the server with the specified port
    main(port=args.port)
