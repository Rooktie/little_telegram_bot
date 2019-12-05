import requests
from bs4 import BeautifulSoup

main_link = "https://gorodche.ru/news/"

r = requests.get(main_link)
c = r.content
soup = BeautifulSoup(c, "html.parser")

# place for save news
news_to_message = {}

main_news_block = soup.find(
    "div", class_="news-grid clearfix").find_all("div", class_="news-grid__elem")
source_for_first_news = main_news_block[0].find(
    "div", class_="news-piece news-piece_major").find("a")
text_of_first_news = source_for_first_news.text
link_of_first_news = main_link.strip("/news/") + source_for_first_news["href"]
news_to_message[text_of_first_news] = link_of_first_news

for item in main_news_block[1:]:
    all_news_in_block = item.find_all("div", class_="news-piece")
    for item in all_news_in_block:
        news_text = item.find("a").text
        news_to_message[news_text] = main_link.strip(
            "/news/") + item.find("a")["href"]


def tell_news():
    news_to_str = ""
    for key, value in news_to_message.items():
        news_to_str += key + "\n" + value + "\n\n"
    return news_to_str