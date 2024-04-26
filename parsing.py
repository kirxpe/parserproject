import logging
import requests
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)


def get_hacker_news_links():
    url = "https://news.ycombinator.com/newest"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем статус ответа
    except requests.exceptions.RequestException as e:
        logging.error(f"Ошибка при запросе к {url}: {e}")
        return []

    html_content = response.content
    soup = BeautifulSoup(html_content, features="html.parser")
    links = []
    for thing in soup.find_all("tr", class_="athing"):
        link_element = thing.find("span", class_="titleline").find("a")
        if link_element:
            title = link_element.text.strip()
            news_link = link_element.get("href")
            links.append({"title": title, "url": news_link})  # Словарь с данными

    logging.info(f"Извлечено {len(links)} ссылок")
    return links
