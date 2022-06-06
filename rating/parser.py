import requests
from bs4 import BeautifulSoup as bs
import csv

url = 'https://vesti.kg/'


def get_html(url):
    res = requests.get(url).text
    return res

a = []
def get_data(html):
    soup = bs(html, 'lxml')
    vesti = soup.find_all('div', class_='itemContainer itemContainerLast')

    for i in vesti:
        novosti = i.find('h2').text.strip()
        owner = i.find('p').text.strip()
        date = i.find('span').text.strip()
        image = i.find('a').get('href')
        a.append(novosti)
        a.append(owner)
        a.append(date)
        a.append(url + image)

    return a



get_data(get_html(url))