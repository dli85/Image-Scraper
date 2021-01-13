from bs4 import BeautifulSoup
import requests

class imageCollector:
    def __init__(self, link):
        self.link = link
        self.soupData = BeautifulSoup(requests.get(link).text, 'html.parser')
        self.title = self.soupData.findAll('h1')[0].getText().replace(',', '')
        print(self.title)

        self.imageLinks = []

        for i in self.soupData.find_all('img'):
            self.imageLinks.append(i['src'])

