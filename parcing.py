from bs4 import BeautifulSoup
import requests
import csv

#Список фильмов, которые идут сегодня
URL = 'https://kinoteatr.ru/raspisanie-kinoteatrov/sankt-peterburg/rodeo-drive/'

html = requests.get(URL).text

soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all('div', class_ = 'shedule_movie_description')

films = list()
for item in items:
    name = item.find('span', class_ = 'movie_card_header title').get_text().replace(',',' ').replace("\n", " ").replace('                       ','').replace('                     ','')
    description = item.find('span', class_ = 'movie_card_raiting sub_title').get_text().replace(',',' ').replace("\n", " ").replace('                       ','').replace('                     ','')
    age = item.find('i', class_ = 'raiting_sub').get_text().replace(',',' ').replace("\n", " ").replace('                       ','').replace('                     ','')

    films.append({
        'Название': name,
        'Жанр': description,
        'Ограничение': age
        })

    #print(films)

with open('films.csv', 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['Название', 'Жанр', 'Ограничение'])

    for i in films:
        writer.writerow([i['Название'], i['Жанр'], i['Ограничение']])

