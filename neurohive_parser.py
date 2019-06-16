import requests
import bs4
import datetime
import interaction_db


def neurohive_parser():
    r = requests.get('https://neurohive.io/ru/')
    response = bs4.BeautifulSoup(r.text, "html.parser")
    titel = response.select('.desc')[0].getText()

    matches_in_db = interaction_db.search_in_db('neurohive.io/ru/', titel)

    if not matches_in_db:
        href = 'https://neurohive.io/ru/' + response.select('.desc a')[0].get('href')
        date = datetime.datetime.today().strftime("%m/%d/%Y")
        interaction_db.update_data('neurohive.io/ru/', titel, href, date)





