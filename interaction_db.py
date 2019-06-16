import pymysql.cursors
import send_msg


def add_new_data(site_name, titel, href, date):
    sql = "INSERT INTO news (site_name, title, href, date) VALUES (%s, %s, %s, %s) "
    with connection.cursor() as cursor:
        cursor.execute(sql, (site_name, titel, href, date))
    send_msg.send_msg(site_name, titel, href, date)
    connection.commit()
    

def update_data(site_name, titel, href, date):

    connection = pymysql.connect(host='127.0.0.1',
                                user='nikben',
                                password='08112001Nek',
                                db='news_parser',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    
    try:
        sql = "UPDATE news SET title= %s, href= %s, date= %s WHERE site_name = '" + site_name + "'"
        with connection.cursor() as cursor:
            cursor.execute(sql, (titel, href, date))
        send_msg.send_msg(site_name, titel, href, date)
        connection.commit()
    finally:
        connection.close()
        

def search_in_db(site_name, title):

    connection = pymysql.connect(host='127.0.0.1',
                                user='nikben',
                                password='08112001Nek',
                                db='news_parser',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    response = False
    
    try:
        sql = " SELECT news_id, site_name, title, href, date FROM news WHERE title = '" + title + "' AND site_name = '" + site_name + "'"

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) != 0:
                response = rows
    finally:
        connection.close()
        
    return response
