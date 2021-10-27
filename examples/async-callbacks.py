import asyncio
from time import time
from httpx import AsyncClient


async def scrape(url, session):
    return await session.get(url)

def collect(result):
    print(result)

async def run():
    _start = time()
    async with AsyncClient() as session:
        for i in range(100):
            # this url will always take 1 second
            url = "http://httpbin.org/delay/1"
            task = asyncio.create_task(scrape(url, session=session))
            task.add_done_callback(collect)
        await asyncio.all_tasks()
        await asyncio.sleep(5)
    print(f"finished scraping in: {time() - _start:.1f} seconds")


if __name__ == "__main__":
    asyncio.run(run())
