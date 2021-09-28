import re
from typing import List

import requests
from parsel import Selector


def parse_sitemap(url: str) -> List[str]:
    """scrape sitemap and item urls from a sitemap link"""
    print(f"scraping: {url}")
    resp = requests.get(
        url,
        headers={
            # we need to fake browser user-string to get through CDN bot protection
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
        },
    )
    # turn html text to a parsable tree object
    doc_tree = Selector(resp.text)
    # find all <loc> nodes and take their text (which is an url)
    urls = doc_tree.xpath("//loc/text()").getall()
    return urls


product_urls = set()
sitemap_directory = "https://www2.hm.com/en_us.sitemap.xml"
for url in parse_sitemap(sitemap_directory):
    if ".product." not in url:
        continue
    for url in parse_sitemap(url):
        # product urls match pattern com/<some product naming>.html
        # skip non-product urls
        if not re.search(r"hm.com/.+?\.html", url):
            continue
        product_urls.add(url)
print("\n".join(product_urls)[-100:])
print(len(product_urls))
