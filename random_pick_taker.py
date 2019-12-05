import requests
import random
from bs4 import BeautifulSoup

main_link = "http://yande.re/post"


def get_link_on_page_with_images():
    r = requests.get(main_link)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    last_page = int(
        soup.find("div", class_="pagination").find_all("a")[-2].text)
    random_page = random.randint(1, last_page)
    return main_link + "?page=" + str(random_page)


def generate_image_link():
    r = requests.get(get_link_on_page_with_images())
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all_pics_on_page = soup.find_all("a", class_="directlink largeimg")
    num_of_random_pic = random.randint(1, len(all_pics_on_page))
    return all_pics_on_page[num_of_random_pic - 1]["href"]

# save image in file
# if __name__ == "__main__":
#     r = requests.get(link_on_pic, stream=True)
#     with open(link_on_pic[-10:].strip("%/\\-!-#$&*^@"), "bw") as f:
#         for chunk in r.iter_content(8192):
#             f.write(chunk)
