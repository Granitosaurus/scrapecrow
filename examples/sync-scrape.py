from httpx import Client
from time import time


def scrape(url, session):
    return session.get(url)


def run():
    _start = time()
    results = []
    with Client() as session:
        for i in range(100):
            # this url will always take 1 second
            url = "http://httpbin.org/delay/1"
            results.append(scrape(url, session=session))
    print(f"finished scraping in: {time() - _start:.1f} seconds")


if __name__ == "__main__":
    run()
