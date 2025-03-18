import asyncio

from src.playgrounds.crawl4ai import test_crawl4ai_async


async def run():
    test_crawl4ai_async()
    # tool = EventSearchTool()
    # result = await tool.search(city="leipzig", query="anything")
    # pprint(result)


if __name__ == "__main__":
    asyncio.run(run())
