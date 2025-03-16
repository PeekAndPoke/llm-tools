#!/usr/bin/env python3
"""
Example script demonstrating basic usage of the LLM tools without running the server.
"""

import os
import sys

# Add the parent directory to the path to import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.tools.weather import WeatherTool
    from src.tools.web_search import DuckDuckGoTool
except ImportError as e:
    print(f"Error importing tools: {e}")
    print("Make sure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)


def main():
    """Run the example script."""
    print("LLM-Tools Basic Usage Example")
    print("-----------------------------")

    # Create instances of the tools
    weather_tool = WeatherTool()
    search_tool = DuckDuckGoTool()

    # Example of using the weather tool
    print("\n1. Weather Tool Example:")
    print("------------------------")
    location = "San Francisco"
    print(f"Getting weather for: {location}")

    try:
        weather_result = weather_tool._run(location)
        print(f"Current temperature: {weather_result['current']['temperature']}°C")
        print(f"Condition: {weather_result['current']['condition']}")
        print(
            f"Forecast: {weather_result['forecast'][0]['condition']} (High: {weather_result['forecast'][0]['temp_high']}°C, Low: {weather_result['forecast'][0]['temp_low']}°C)")
    except Exception as e:
        print(f"Error using weather tool: {e}")

    # Example of using the search tool
    print("\n2. Web Search Tool Example:")
    print("--------------------------")
    query = "Python programming language"
    print(f"Searching for: {query}")

    try:
        search_results = search_tool._run(query, num_results=2)
        for i, result in enumerate(search_results, 1):
            print(f"\nResult {i}:")
            print(f"Title: {result['title']}")
            print(f"URL: {result['url']}")
            print(f"Snippet: {result['snippet'][:100]}...")
    except Exception as e:
        print(f"Error using search tool: {e}")

    print("\nNote: These examples use mock data. For real data, implement API integrations.")


if __name__ == "__main__":
    main()
