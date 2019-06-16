import vk_api
from random import randint

vk_session = vk_api.VkApi(token='pcw456988bd968f48b8c4334cbc3bc60fc84f75590f42182744706d8lw984iw8scb8e40e52d4409og2c3')
vk = vk_session.get_api()



def send_msg(site_name, title, href, date):
    response = site_name + '\n ' + title + '\n ' + date + '\n ' + href
    vk.messages.send(user_id=126766515, message=response, random_id=randint(1, 2000))