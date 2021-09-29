import logging
import asyncio
import re
from urllib.parse import urlparse
from typing import List
from parsel import Selector
from httpx import AsyncClient


class HMScraper:
    save_urls = re.compile("/productpage\.")  # e.g ...com/en_us/productpage.09008.html
    follow_urls = re.compile("\.html")
    follow_saved_urls = False

    def __init__(self, limit=5):
        self.limiter = asyncio.Semaphore(limit)
        self.log = logging.getLogger(type(self).__name__)
        self.seen_urls = set()

    async def __aenter__(self):
        """on scraper creation open http session"""
        self.session = AsyncClient(
            # we should use a browser-like user agent header to avoid being blocked
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
            }
        )
        return self

    async def __aexit__(self, *args):
        """on scraper destruction close http session"""
        await self.session.aclose()

    async def _request(self, url: str):
        async with self.limiter:
            try:
                resp = await self.session.get(url)
            except Exception as e:
                return e
            return resp

    async def save(self, url):
        print(url)

    async def scrape(self, urls: List[str]):
        """Breadth first"""
        while True:
            to_follow = set()
            for resp in asyncio.as_completed([self._request(url) for url in urls]):
                resp = await resp
                if isinstance(resp, Exception):
                    continue
                if resp.status_code != 200:
                    continue
                for url in self.find_links(resp):
                    if self.save_urls.search(url):
                        await self.save(url)
                        if not self.follow_saved_urls:
                            continue
                    if self.follow_urls.search(url):
                        print(f"  following {url}")
                        to_follow.add(url)
            if to_follow:
                urls = to_follow
            else:
                return  # end of the crawl

    def find_links(self, resp, only_unique=True):
        """
        find all relative page links in html link nodes
        """
        # build a parsable tree from html body
        sel = Selector(resp.text)
        current_url_parts = urlparse(str(resp.url))
        # find all <a> nodes and select their href attribute
        urls = sel.xpath("//a/@href").extract()
        for url in urls:
            # convert relative url to absolute
            if url.startswith("/"):
                url = current_url_parts._replace(path=url).geturl()
            # skip absolute urls that do not match current domain
            if urlparse(url).netloc != current_url_parts.netloc:
                continue
            # skip visited urls
            if only_unique and url in self.seen_urls:
                continue
            self.seen_urls.add(url)
            yield url


async def run():
    async with HMScraper() as scraper:
        start_urls = [
            # homepage for US website
            "https://www2.hm.com/en_us/index.html"
        ]
        await scraper.scrape(start_urls)


if __name__ == "__main__":
    asyncio.run(run())
