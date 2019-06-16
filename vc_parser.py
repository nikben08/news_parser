import requests
import bs4
import datetime
import interaction_db



def vc_parser():
    #машинное обучение
    r1 = requests.get('https://vc.ru/search/%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5')
    #искусственный интеллект
    r2 = requests.get('https://vc.ru/search/%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82')
    #нейронный сети
    r3 = requests.get('https://vc.ru/search/%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%81%D0%B5%D1%82%D0%B8')

    response1 = bs4.BeautifulSoup(r1.text, "html.parser")
    response2 = bs4.BeautifulSoup(r2.text, "html.parser")
    response3 = bs4.BeautifulSoup(r3.text, "html.parser")

    titel1 = response1.select('.b-article h2')[0].getText().rstrip().lstrip()
    titel2 = response2.select('.b-article h2')[0].getText().rstrip().lstrip()
    titel3 = response3.select('.b-article h2')[0].getText().rstrip().lstrip()

    matches_in_db1 = interaction_db.search_in_db('vc.ru/tag/ml/', titel1)
    matches_in_db2 = interaction_db.search_in_db('vc.ru/tag/ai/', titel2)
    matches_in_db3 = interaction_db.search_in_db('vc.ru/tag/nn/', titel3)

    if not matches_in_db1:
        date1 = datetime.datetime.today().strftime("%m/%d/%Y")
        href1 = response1.select('.entry_content__link')[0].get('href')
        interaction_db.update_data('vc.ru/tag/ml/', titel1, href1, date1)

    if not matches_in_db2:
        date2 = datetime.datetime.today().strftime("%m/%d/%Y")
        href2 = response2.select('.entry_content__link')[0].get('href')
        interaction_db.update_data('vc.ru/tag/ai/', titel2, href2, date2)

    if not matches_in_db3:
        date3 = datetime.datetime.today().strftime("%m/%d/%Y")
        href3 = response3.select('.entry_content__link')[0].get('href')
        interaction_db.update_data('vc.ru/tag/nn/', titel3, href3, date3)

