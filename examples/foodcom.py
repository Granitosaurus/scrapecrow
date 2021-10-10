import requests

headers = {
    # when web scraping we always want to appear as 
    # a web browser to prevent being blocked
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
data = {
    # our recipe search term
    "searchTerm": "Toast",
    # page number
    "pn": 1,
}

url = "https://api.food.com/external/v1/nlp/search"
response = requests.post(url, json=data)

data = response.json()
results = data["response"]["results"]
total_results_count = data["response"]["totalResultsCount"]
print(f"found {len(results)} results from {total_results_count} total")
# this will print: "found 10 results from 2246 total"
