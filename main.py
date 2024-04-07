import requests
from bs4 import BeautifulSoup
import schedule
import time

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

hacker_news_list = get_hacker_news_links()
print(hacker_news_list)