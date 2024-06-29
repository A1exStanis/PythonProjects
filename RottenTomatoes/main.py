import requests
from bs4 import BeautifulSoup
import constant
import csv

response = requests.get(constant.URL)
soup = BeautifulSoup(response.text, constant.FORMAT)
films = soup.findAll(constant.DIV, class_=constant.CLASS_FLEX_CONT)
data = []

for film in films:
    link = constant.MAIN_URL + film.find(constant.TAG_A).get(constant.HREF)
    name = (film.find(constant.TAG_A).find(constant.TAG_SPAN, class_=constant.CLASS_P_SMALL)
            .text.strip())
    date = film.find(constant.TAG_A).find(constant.TAG_SPAN, class_=constant.CLASS_SMALLER).text.strip()
    score = film.find(constant.TAG_A).findAll(constant.TAG_RT)
    try:
        audience_score = score[0].text
    except:
        audience_score = '-'
    try:
        critics_score = score[1].text
    except:
        critics_score = '-'
    data.append([name, date, link, audience_score, critics_score])

with open('NewFilms.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Realise Date', 'Link', 'Audience Score', 'Critics Score'])
    for film in data:
        writer.writerow(film)
