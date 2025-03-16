"""
Tests for LLM-Tools tools functionality.
"""

import importlib.util

import pytest

# Check if langchain is available
langchain_available = importlib.util.find_spec("langchain") is not None

# Import tools (mark tests as skipped if langchain not available)
if langchain_available:
    from src.tools.weather import WeatherTool
    from src.tools.web_search import DuckDuckGoTool
else:
    pytest.skip("langchain not installed", allow_module_level=True)


class TestWeatherTool:
    """Tests for the weather forecast tool."""

    def test_weather_tool_run(self):
        """Test that the weather tool returns expected format for a location."""
        tool = WeatherTool()
        result = tool._run("New York")

        # Check that result has expected structure
        assert "location" in result
        assert result["location"] == "New York"
        assert "current" in result
        assert "temperature" in result["current"]
        assert "forecast" in result
        assert isinstance(result["forecast"], list)

    def test_weather_tool_name_and_description(self):
        """Test that the weather tool has proper name and description."""
        tool = WeatherTool()
        assert tool.name == "weather_forecast"
        assert "weather forecast" in tool.description.lower()


class TestWebSearchTool:
    """Tests for the web search tool."""

    def test_web_search_tool_run(self):
        """Test that the web search tool returns expected format for a query."""
        tool = DuckDuckGoTool()
        results = tool._run("test query", num_results=2)

        # Check that results have expected structure
        assert isinstance(results, list)
        assert len(results) == 2  # We requested 2 results

        # Check first result structure
        assert "title" in results[0]
        assert "snippet" in results[0]
        assert "url" in results[0]

    def test_web_search_tool_name_and_description(self):
        """Test that the web search tool has proper name and description."""
        tool = DuckDuckGoTool()
        assert tool.name == "web_search"
        assert "search" in tool.description.lower()
