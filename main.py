import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

def get_hacker_news_links():
    url = "https://news.ycombinator.com/newest"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, features='html.parser')
    links = []
    for thing in soup.find_all('tr', class_="athing"):
        link_element = thing.find("span", class_="titleline").find("a")
        if link_element:
            news_link = link_element.get("href")
            links.append(news_link)

    return links

app = FastAPI()

@app.get("/test")
def get_info():
    links = get_hacker_news_links()
    return links




