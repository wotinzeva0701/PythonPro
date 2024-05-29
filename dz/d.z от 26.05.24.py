import requests
from bs4 import BeautifulSoup


class NewsParser:
    def __init__(self):
        self.base_url = 'https://650kirov.ru'
        self.news_data = []

    def fetch_page(self, url):
        response = requests.get(url)
        return response.text

    def parse_news(self, html):
        soup = BeautifulSoup(html, 'lxml')
        news_blocks = soup.find_all('div', class_='caption')

        for block in news_blocks:
            title = block.find('h3').text.strip()
            link = self.base_url + block.find('a')['href']
            author = block.find('a', class_='topic-info-author-link').text.strip()

            news_item = {
                'title': title,
                'link': link,
                'author': author
            }

            self.news_data.append(news_item)

    def run(self):
        for page_num in range(1, 4):
            url = f'{self.base_url}/page/{page_num}'
            page_html = self.fetch_page(url)
            self.parse_news(page_html)

    def print_news(self):
        for idx, news_item in enumerate(self.news_data, start=1):
            print(f'Новость {idx}:')
            print(f'Заголовок: {news_item["title"]}')
            print(f'Ссылка: {news_item["link"]}')
            print(f'Автор: {news_item["author"]}')
            print()


parser = NewsParser()
parser.run()

parser.print_news()
