import asyncio
from time import time
from playwright.async_api._context_manager import PlaywrightContextManager
from loguru import logger as log
from typing import Optional, Dict, Literal


class BrowserPool:
    def __init__(
        self,
        pool_size=5,
        browser_type: Literal["chromium", "firefox"] = "chromium",
        browser_kwargs: Optional[Dict] = None,
    ) -> None:
        self.pool_size = pool_size
        self.browser_type = browser_type
        self.browser_kwargs = browser_kwargs or {}
        self.pool = {}
        self.pw_manager = None
        self.pw = None

    async def __aenter__(self):
        log.info(f"opening browser pool with {self.pool_size} {self.browser_type}({self.browser_kwargs}) browser instances")
        self.pw_manager = PlaywrightContextManager()
        self.pw = await self.pw_manager.__aenter__()
        await asyncio.gather(*[self.start_browser(i) for i in range(self.pool_size)])
        return self

    async def __aexit__(self, *args):
        log.debug("closing browser pool and all attached browsers")
        for browser, page in self.pool.values():
            await browser.close()
        await self.pw_manager.__aexit__(*args)

    async def start_browser(self, name: str):
        log.debug(f"starting browser {name}")
        browser = await getattr(self.pw, self.browser_type).launch(
            **self.browser_kwargs
        )
        browser.is_busy = False
        browser.name = name
        page = await browser.new_page()
        self.pool[name] = browser, page

    async def get_browser(self):
        while True:
            for browser, page in self.pool.values():
                if not browser.is_busy:
                    browser.is_busy = True
                    return browser, page
                await asyncio.sleep(0.01)  # need to leave open frame here

    async def get_page(self, url, wait_for_css=None, wait_for_load="domcontentloaded"):
        for i in range(5):
            log.debug(f"{url}: looking for idle browser")
            browser, page = await self.get_browser()
            log.info(f"{url}: using browser {browser.name}")
            try:
                await page.goto(url)
                async with page.expect_event("response") as event_info:
                    doc_response = await event_info.value 
                await page.wait_for_load_state(wait_for_load)
                if wait_for_css:
                    await page.wait_for_selector(wait_for_css)
                content = await page.content()
            except Exception as e:
                # browser went under - restart browser and retry
                log.warning(f"{url}: restarting browser {browser.name} got {e}; retry {i}/5")
                await self.start_browser(browser.name)
                continue
            browser.is_busy = False
            return {
                "url": page.url,
                "content": len(content),  # todo unwrap
                "status_code": doc_response.status,
            }
        raise e
        


if __name__ == "__main__":

    async def run():
        start = time()
        async with BrowserPool(3, "chromium", {"headless": False}) as pool:
            urls = [
                "https://www.airbnb.com/experiences/2496585",
                "https://www.airbnb.com/experiences/2488061",
                "https://www.airbnb.com/experiences/2563542",
                "https://www.airbnb.com/experiences/3010357",
                "https://www.airbnb.com/experiences/2624432",
                "https://www.airbnb.com/experiences/3033250",
            ]
            for content in asyncio.as_completed([pool.get_page(url) for url in urls]):
                content = await content
                print(f"got page length of {content}")
        log.info(f"finished scraping {len(urls)} urls in {time() - start:.1f}")

    asyncio.run(run())
