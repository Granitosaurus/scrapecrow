import asyncio
from time import time
from httpx import AsyncClient


async def scrape(url, session, throttler):
    async with throttler:
        return await session.get(url)


async def run():
    _start = time()
    throttler = asyncio.Semaphore(10)
    async with AsyncClient() as session:
        tasks = []
        for i in range(100):
            # this url will always take 1 second
            url = "http://httpbin.org/delay/1"
            tasks.append(scrape(url, session=session, throttler=throttler))
        results = await asyncio.gather(*tasks)
    print(f"finished scraping in: {time() - _start:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(run())
