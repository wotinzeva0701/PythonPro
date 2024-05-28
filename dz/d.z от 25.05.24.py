import csv

import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    res = re.sub(r"\D+", "", s)
    return res


def write_csv(data):
    with open("market_data.csv", "a") as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=";")
        writer.writerow((data['name'], data['url'], data['price']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    products = soup.find_all("div", class_="catalog_element")

    for product in products:
        name = product.find("div", class_="catalog_title").text
        url = product.find("a", class_="link catalog_image_link").get("href")
        price = product.find("span", class_="catalog_price").text
        refined_price = refined(price)
        data = {'name': name, 'url': url, 'price': refined_price}
        write_csv(data)


def main():
    url = "https://market-kirov.ru/"
    (get_data(get_html(url)))


if __name__ == '__main__':
    main()
