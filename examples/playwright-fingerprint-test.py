import asyncio
from playwright.async_api import async_playwright


async def read_fingerprint():
    async with async_playwright() as pw:
        # launch 3 browsers
        browser = await pw.chromium.launch()
        # start 1 tab each on every browser
        page = await browser.new_page()
        await page.goto("https://abrahamjuliot.github.io/creepjs/")
        await asyncio.sleep(5)
        screenshot = await page.screenshot(type="png", full_page=True)
        with open("playwright-fingerprint-test.png", "wb") as f:
            f.write(screenshot)


if __name__ == "__main__":
    asyncio.run(read_fingerprint())
