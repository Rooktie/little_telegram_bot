import requests
import random
from bs4 import BeautifulSoup, UnicodeDammit
from fake_useragent import UserAgent

main_link = "https://bash.im/random"
r = requests.get(main_link)
c = r.content
soup = BeautifulSoup(c, "html.parser")

all_quotes = soup.find_all("div", class_="quote")[:-1]


def end_text():
    text_of_qoute = UnicodeDammit(str(all_quotes[random.randint(1, len(all_quotes)) - 1].find(
        "div", class_="text"))[18:-6].replace("<br/>", "\n").replace("<br>", "").replace("</br>", ""))
    return text_of_qoute.unicode_markup