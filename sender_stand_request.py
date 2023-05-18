import data
import configuration
import requests

#Создание нового пользователя для тестрана
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#Создание нового набора для функции проверок
def post_new_client_kit(kit_body,auth_token):
    auth_headers = data.headers.copy()
    auth_headers["Authorization"] = "Bearer " + auth_token #по комментарию понял что тут вроде ничего исправлять не надо
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=auth_headers)
