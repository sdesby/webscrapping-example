import urllib2
from bs4 import BeautifulSoup
import csv

url = "http://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1"
html_page = urllib2.urlopen(url)

soup = BeautifulSoup(html_page, "html.parser")

# print soup.prettify()

list_items = soup.findAll('div', class_='list_item')

titles = []
directors = []

for item in list_items:
    h4 = item.find('h4')
    a = h4.find('a')
    titles.append(a.string)

print titles

for item in list_items:
    txt_block = item.find('div', class_="txt-block")
    link_director = txt_block.find('a')
    directors.append(link_director.string)

print directors

with open('titles_imdb.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Title", "Director"])

    index = 0
    while index < len(titles):
        writer.writerow([titles[index].encode('utf-8'), directors[index].encode('utf-8')])
        index += 1
