import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        souvenir = self.html.find_all("div", class_="col-12 col-sm-6 col-lg-3")
        for item in souvenir:
            title_elem = item.find('h3')
            href_elem = item.find('a')
            text_elem = item.find('a', class_="card__title-link")

            if title_elem and href_elem and text_elem:
                title = title_elem.text.strip()
                href = href_elem.get('href')

                self.res.append({
                    "title": title,
                    "href": href,

                })

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Интересные места {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\n\n{'*' * 50}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


def main():
    pars = Parser("https://650kirov.ru/tourists/#souvenir", "souvenir.txt")
    pars.run()


if __name__ == '__main__':
    main()
