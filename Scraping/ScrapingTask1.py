import requests
from bs4 import BeautifulSoup

from Scraping.IntroToScraping import Proxyfactory

mproxy = Proxyfactory()
proxies_pool, headers_pool = mproxy.create_pools()
current_proxy = next(proxies_pool)
current_headers = next(headers_pool)

# Introduce the proxy and headers in the GET request
with requests.Session() as req:
    page = req.get("http://www.nytimes.com/")
    soup = BeautifulSoup(page.text, 'html.parser')
    headlines = soup.find_all("h2", {"class": "css-z9cw67 e1voiwgp0"})
    for t in headlines:
        print(t.text)
