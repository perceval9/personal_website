from bs4 import BeautifulSoup
import requests

page_to_scrape = 'https://www.bbc.co.uk/news'
soup = BeautifulSoup(requests.get(page_to_scrape).content, 'html.parser')