import requests
from time import sleep, time

url = "https://www.binance.com/en/support/announcement/c-49?navId=49"
last_known_version = None
session = requests.session()
_start = time()
history = []
while True:
    resp = session.head(url, headers={"Cache-Control": "no-store"})
    current_version = resp.headers["via"]
    # new verison has been seen
    if current_version != last_known_version:
        history.append(current_version)
        print(history)
        # resp = session.get(url)
        last_known_version = current_version
    else:  # nothing has ehcnaged
        sleep(1)
        continue
        
print(f"finished in {_start - time()}")
