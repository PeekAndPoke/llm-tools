"""
Weather forecast tool for LLM integration using MCP protocol.
Uses a weather API to provide forecasts for given locations.
"""

from typing import Dict, Any, Optional

from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools import BaseTool


class WeatherTool(BaseTool):
    """Tool for getting weather forecasts for locations."""

    name: str = "weather_forecast"
    description: str = "Get weather forecast for a specific location"

    def _run(
            self,
            location: str,
            run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> Dict[str, Any]:
        """
        Get the weather forecast for a specific location.

        Args:
            location: The city or location to get the forecast for
            run_manager: Callback manager for the tool run

        Returns:
            Dict containing weather data including temperature, conditions, etc.
        """
        # Here we would use a real weather API like OpenWeatherMap
        # For now, return mock data as placeholder

        # TODO: Implement actual API integration
        mock_response = {
            "location": location,
            "current": {
                "temperature": 22.5,
                "feels_like": 23.0,
                "humidity": 65,
                "condition": "Partly cloudy",
                "wind_speed": 12.0,
                "wind_direction": "NE"
            },
            "forecast": [
                {
                    "day": "Today",
                    "temp_high": 24.0,
                    "temp_low": 18.0,
                    "condition": "Partly cloudy"
                },
                {
                    "day": "Tomorrow",
                    "temp_high": 26.0,
                    "temp_low": 19.0,
                    "condition": "Sunny"
                }
            ]
        }

        return mock_response

    def _arun(
            self,
            location: str,
            run_manager: Optional[CallbackManagerForToolRun] = None
    ):
        """Async implementation of the weather tool."""
        # Will implement proper async version when integrating with actual API
        raise NotImplementedError("Async version not implemented yet")
