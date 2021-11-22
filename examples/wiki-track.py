from time import sleep
import requests

session = requests.Session()
last_modified = None
url = "https://en.wikipedia.org/wiki/Web_scraping"
while True:
    resp_head = session.head(url)
    if resp_head.headers['Last-Modified'] != last_modified:
        last_modified = resp_head.headers['Last-Modified']
        print("change detected!")
        # additionally we can full response for better notification details
        resp_full = session.get(url)
        print(resp_full)
    sleep(1)
