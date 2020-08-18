
# Introduce the proxy and headers in the GET request
import requests
from bs4 import BeautifulSoup
title_dict ={}
calls=0#safety to prevent server overload
with requests.Session() as req:
    page = req.get("http://recurship.com/")
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all("a", {"class": "post-thumbnail"})
    for t in links:
        link = t.get('href')
        linkPage=req.get(link)
        calls+=1
        soup = BeautifulSoup(linkPage.text, 'html.parser')
        title= soup.find('title').text
        title_dict[title]=[]
        images = soup.findAll('img')
        for image in images:
            title_dict[title].append(image['src'])

        if(calls>40):
            break
print(title_dict)
