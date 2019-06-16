import requests
import bs4
import datetime
import interaction_db


def hi_news_parser():
    r1 = requests.get('https://hi-news.ru/tag/mashinnoe-obuchenie')
    r2 = requests.get('https://hi-news.ru/tag/iskusstvennyj-intellekt')

    response1 = bs4.BeautifulSoup(r1.text, "html.parser")
    response2 = bs4.BeautifulSoup(r2.text, "html.parser")

    titel1 = response1.select('h2')[0].getText().rstrip().lstrip()
    titel2 = response2.select('h2')[0].getText().rstrip().lstrip()
    matches_in_db1 = interaction_db.search_in_db('hi-news.ru/tag/mashinnoe-obuchenie/', titel1)
    matches_in_db2 = interaction_db.search_in_db('hi-news.ru/tag/iskusstvennyj-intellekt/', titel2)

    if not matches_in_db1:
        href1 = response1.select('h2 a')[0].get('href')
        date1 = datetime.datetime.today().strftime("%m/%d/%Y")
        interaction_db.update_data('hi-news.ru/tag/mashinnoe-obuchenie/', titel1, href1, date1)

    if not matches_in_db2:
        href2 = response2.select('h2 a')[0].get('href')
        date2 = datetime.datetime.today().strftime("%m/%d/%Y")
        interaction_db.update_data('hi-news.ru/tag/iskusstvennyj-intellekt/', titel2, href2, date2)






