import asyncio
from pprint import pprint

from src.tools.eventsearch import EventSearchTool


async def run():
    tool = EventSearchTool()

    result = await tool.search(city="leipzig", query="anything")

    pprint(result)


if __name__ == "__main__":
    asyncio.run(run())
