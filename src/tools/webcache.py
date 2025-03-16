from datetime import timedelta
from typing import Optional

from diskcache import Cache


class WebContentCache:
    def __init__(self, cache_dir='.webcache', expire_hours=3):
        self.cache = Cache(cache_dir)
        self.expire_seconds = int(timedelta(hours=expire_hours).total_seconds())

    def get_content(self, url: str) -> Optional[str]:
        # Try to get from cache first
        if url in self.cache:
            return self.cache[url]

        return None

    def set_content(self, url: str, content: str):
        self.cache.set(url, content, expire=self.expire_seconds)

    def clear(self):
        self.cache.clear()
