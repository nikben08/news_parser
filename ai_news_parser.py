import requests
import bs4
import datetime
import interaction_db


def ai_news_parser():
    r = requests.get('http://ai-news.ru/')
    response = bs4.BeautifulSoup(r.text, "html.parser")
    titel = response.select('.toprighttxt a')[0].getText().rstrip().lstrip()

    matches_in_db = interaction_db.search_in_db('ai-news.ru/', titel)

    if not matches_in_db:
        href = 'http://ai-news.ru/' + response.select('.toprighttxt a')[0].get('href')
        date = datetime.datetime.today().strftime("%m/%d/%Y")
        interaction_db.update_data('ai-news.ru/', titel, href, date)






