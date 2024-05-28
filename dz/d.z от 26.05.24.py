import csv

import requests
from bs4 import BeautifulSoup

def main():
    for i in range(3, 4):
        url = f""
        get_data(get_html(url))