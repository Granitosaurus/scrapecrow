import asyncio
from asyncio import gather
from playwright.async_api import async_playwright
from playwright.async_api._generated import Page


async def scrape_3_pages_concurrently():
    async with async_playwright() as pw:
        # launch 3 browsers
        browsers = await gather(*(pw.chromium.launch() for _ in range(3)))
        # start 1 tab each on every browser
        pages = await gather(*(browser.new_page() for browser in browsers))

        async def get_loaded_html(page: Page, url: str):
            """"""
            await page.goto(url)
            await page.wait_for_load_state("domcontentloaded")
            return url, await page.content()

        # scrape 3 pages concurrently on 3 different pages
        urls = [
            "https://www.airbnb.com/experiences/2496585",
            "https://www.airbnb.com/experiences/2488061",
            "https://www.airbnb.com/experiences/2563542",
            # "http://url1.com",
            # "http://url2.com",
            # "http://url3.com",
        ]
        htmls = await gather(*(
            get_loaded_html(page, url)
            for page, url in zip(pages, urls)
        ))
        return htmls


if __name__ == "__main__":
    asyncio.run(scrape_3_pages_concurrently())
