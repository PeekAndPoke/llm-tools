"""
Tools package for LLM-Tools, providing various capabilities to LLMs.
"""

from src.tools.duckduckgo import DuckDuckGoTool
from src.tools.weather import WeatherTool

__all__ = ["WeatherTool", "DuckDuckGoTool"]
