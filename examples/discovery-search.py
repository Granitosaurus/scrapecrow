from typing import Dict
import httpx
import asyncio


async def scrape_page(
    session: httpx.AsyncClient,
    offset=0,
    page_size=500,  # note: we can increase this from default 40 to something higher!
    sort="ascPrice",
) -> Dict:
    """Scrape a single hm.com product query page"""
    url = "https://www2.hm.com/en_us/search-results/_jcr_content/search.display.json"
    print(f"scraping range {offset}:{offset+page_size} sorted by: {sort}")
    response = await session.get(
        url=url,
        timeout=httpx.Timeout(120),
        params={
            "q": " ",  # note: http client will automatically turn this to "%20"
            "offset": offset,
            "page-size": page_size,
            "sort": sort,
        },
    )
    return response.json()


async def scrape_hmcom():
    # we need to fake any browser User-Agent to get around primitive bot detection
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
    }
    products = []
    async with httpx.AsyncClient(headers=headers) as session:
        # lets start by scraping first page
        first_page = await scrape_page(session)
        products.extend(first_page["products"])

        # First page contains total amount of results this query contains
        # using this we can create task for each bach of query and
        # execute it concurrently
        tasks = []
        for offset in range(
            first_page["itemsShown"], first_page["total"], first_page["itemsShown"]
        ):
            # for first 10_000 scrape as usual
            if offset < 10_000:
                sorting = "ascPrice"
            # for query > 10_000 start over with reversed ordering
            else:
                sorting = "descPrice"
                offset -= 10_000
            tasks.append(scrape_page(session, offset=offset, sort=sorting))
        print(f"Scheduling {len(tasks)} scrape tasks concurrently")

        # with our scraping tasks in order it's time
        # to execute them concurrently using asyncio.as_completed wrapper
        for scrape_task in asyncio.as_completed(tasks):
            result = await scrape_task
            products.extend(result["products"])

    print(f"found {len(products)} products in {len(tasks) + 1} page requests")


if __name__ == "__main__":
    asyncio.run(scrape_hmcom())
