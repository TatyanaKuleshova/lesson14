from bs4 import BeautifulSoup
import requests
import csv

#Список фильмов, которые идут сегодня

URL = 'https://kinomax.ru/#'

html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')
#print(html)

items = soup.find_all('div', class_ = 'd-flex flex-column')

#формируем список, исключая пустые строки

films = list()
for item in items:
    if item.find('div', class_ = 'fs-09 pt-2 post-slick-item') is not None:
        name = item.find('div', class_ = 'fs-09 pt-2 post-slick-item').get_text()
    if item.find('div', class_ = 'fs-09 text-main pt-2 post-slick-item') is not None:
        description = item.find('div', class_ = 'fs-09 text-main pt-2 post-slick-item').get_text()
    if item.find('div', class_ = 'agecategory ml-auto') is not None:
        age = item.find('div', class_ = 'agecategory ml-auto').get_text()

        films.append({
            'Название': name,
            'Жанр': description,
            'Ограничение': age
            })


with open('films.csv', 'a', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file, delimiter='|')

    for i in films:
        writer.writerow([i['Название'], i['Жанр'], i['Ограничение']])

