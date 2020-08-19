import requests
from bs4 import BeautifulSoup


with requests.Session() as req:
    #get the website content
    page = req.get("http://www.nytimes.com/")

    #parsing using article css
    soup = BeautifulSoup(page.text, 'html.parser')
    headlines= soup.select(".e1voiwgp0")
    #headlines = soup.find_all("h2", {"class": "css-z9cw67 e1voiwgp0"})

    #print the headlines
    for t in headlines:
        print(t.text)
