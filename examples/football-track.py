from time import sleep
import requests

session = requests.Session()
last_etag = None
url = "https://onefootball.com/en/match/2263090"
while True:
    resp_head = session.head(url)
    if resp_head.headers["Etag"] != last_etag:
        last_etag = resp_head.headers["Etag"]
        print("change detected!")
        # additionally we can full response for better notification details
        resp_full = session.get(url)
        print(extract_scores_from_response(resp_full))
    sleep(1)
