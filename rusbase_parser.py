import requests
import bs4
import datetime
import interaction_db



def rusbase_parser():
    r1 = requests.get('https://rb.ru/tag/machinelearning/')
    r2 = requests.get('https://rb.ru/tag/ai/')

    response1 = bs4.BeautifulSoup(r1.text, "html.parser")
    response2 = bs4.BeautifulSoup(r2.text, "html.parser")

    titel1 = response1.select('.article-preview__title a')[0].getText()
    titel2 = response2.select('.article-preview__title a')[0].getText()

    matches_in_db1 = interaction_db.search_in_db('rb.ru/tag/machinelearning/', titel1)
    matches_in_db2 = interaction_db.search_in_db('rb.ru/tag/ai/', titel2)

    if not matches_in_db1:
        date1 = datetime.datetime.today().strftime("%m/%d/%Y")
        href1 = 'https://rb.ru' + response1.select('.article-preview__title a')[0].get('href')
        interaction_db.update_data('rb.ru/tag/machinelearning/', titel1, href1, date1)

    if not matches_in_db2:
        date2 = datetime.datetime.today().strftime("%m/%d/%Y")
        href2 = 'https://rb.ru' + response2.select('.article-preview__title a')[0].get('href')
        interaction_db.update_data('rb.ru/tag/ai/', titel2, href2, date2)





