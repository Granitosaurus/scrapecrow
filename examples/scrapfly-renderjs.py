import asyncio

from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse


async def main():
    scrapfly = ScrapflyClient(key="2fbb226543e44335adb496d30c3ba92d", max_concurrency=5)
    to_scrape = [
        # ScrapeConfig(
        #     url="https://www.airbnb.com/experiences/272085",
        #     render_js=True,
        #     wait_for_selector="h1",
        # ),
        ScrapeConfig(
            url="https://abrahamjuliot.github.io/creepjs/",
            render_js=True,
            wait_for_selector=".visitor-info .unblurred",
            screenshots={'full-page': 'fullpage'}
        ),
    ]
    results = await scrapfly.concurrent_scrape(to_scrape)
    with open('scrapfly-renderjs.html', 'w') as f:
        f.write(results[0].content)
    print(results[0].content)

if __name__ == "__main__":
    asyncio.run(main())
