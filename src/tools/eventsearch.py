import uuid
from datetime import datetime, timedelta
from typing import List, Optional
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

from src.tools.webcache import WebContentCache


class EventSearchTool:
    """Tool for performing event searches and retrieving results."""

    def __init__(self):
        self.cache = WebContentCache(cache_dir='.webcache/events', expire_hours=3)

    async def search(self,
                     city: str,
                     from_date: Optional[datetime] = None,
                     to_date: Optional[datetime] = None,
                     query: Optional[str] = None):

        results = []

        current_date = from_date or datetime.now()
        to_date = min((to_date or from_date), current_date + timedelta(days=7))

        while current_date <= to_date:
            params = {
                "start_date__gte": current_date.strftime("%Y-%m-%d"),
                "start_date__lte": current_date.strftime("%Y-%m-%d"),
                "category": "",
            }

            # https://pypi.org/project/Crawl4AI/
            # https://docs.crawl4ai.com/core/content-selection/

            url = f"https://rausgegangen.de/{city.lower()}/eventsearch/?{urlencode(params)}"

            current_results = await self.get_content(url)
            results.extend(current_results)

            current_date += timedelta(days=1)

        return "".join(results)

    async def get_content(self, url: str) -> List[str]:
        """
        Fetch and parse webpage content using BeautifulSoup.

        Args:
            url (str): The URL of the webpage to scrape

        Returns:
            BeautifulSoup: Parsed webpage content or None if request fails
        """

        config = CrawlerRunConfig(
            # e.g., first 30 items from Hacker News
            css_selector=".event-search-result-list",

            cache_mode=CacheMode.ENABLED,
        )

        session_id = uuid.uuid4()

        results: set[str] = set()

        async with AsyncWebCrawler() as crawler:

            for page in range(1, 10):
                paged_url = url + f"&page={page}"

                result_markdown = self.cache.get_content(paged_url)

                if not result_markdown:
                    result = await crawler.arun(
                        session_id=session_id,
                        url=url + f"&page={page}",
                        config=config,
                    )

                    result_markdown = str(result.markdown)

                    self.cache.set_content(paged_url, result_markdown)

                results.add(result_markdown)

        return list(results)
