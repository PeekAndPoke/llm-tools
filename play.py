import asyncio
from pprint import pprint

from src.tools import DuckDuckGoTool


async def run():
    tool = DuckDuckGoTool()

    result = tool.web_search("Metallica")
    pprint(result)

    result = tool.news_search("Metallica")
    pprint(result)

    result = tool.image_search("Metallica")
    pprint(result)

    result = tool.video_search("Metallica")
    pprint(result)

    pass

if __name__ == "__main__":
    asyncio.run(run())
