import sender_stand_request
import data

#Используем функцию post_new_user в файле sender_stand_request.py и берем токен пользователя из 'authToken'
response = sender_stand_request.post_new_user(data.user_body)
auth_token = response.json()['authToken']

#Функция для изменения значения в параметре "name" в теле запроса
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

#Функция для позитивных проверок
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что поле "name" в ответе и запросе совпадают
    assert kit_response.json()["name"] == name

#Функция для негативных проверок
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
    assert response.json()["code"] == 400

def negative_assert_no_data(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
    assert response.json()["code"] == 400

#Удалена функция для негативной провеки без передачи всех необходимых параметров

#Тест №1: Создание набора с допустимым количеством символов в названии, нижняя граница(1)
def test_1_create_kit_1_letter_success():
    positive_assert("a")

#Тест №2: Создание набора с допустимым количеством символов в названии, верхняя граница (511)
# пока искал ответ как сделать запрос функции, успел узнать про значение слеша
def test_2_create_kit_511_success():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест №3: Создание набора с количеством символов меньше допустимого (0)
def test_3_create_kit_0_failed():
    negative_assert("")

#Тест №4: Создание набора с количеством символов больше допустимого (512)
def test_4_create_kit_512_failed():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Тест №5: Создание набора с английкими буквами в названии
def test_5_create_kit_english_success():
    positive_assert("QWErty")

#Тест №6:Создание набора с русскими буквами в названии
def test_6_create_kit_rus_success():
    positive_assert("Мария")

#Тест №7: Создание набора со спецсимволами в названии
def test_7_create_kit_symbol_success():
    positive_assert("\"№%@\",")

#Тест №8: Создание набора с пробелами в названии
def test_8_create_kit_space_success():
    positive_assert("Человек и КО")

#Тест №9: Создание набора с цифрами в названии
def test_9_create_kit_numbers_success():
    positive_assert("123")

#Тест №10: Создание набора без передачи всех необходимых данных
def test_10_create_kit_no_name_failed():
    kit_body = {} #создаем пустой запрос согласно чек-листу
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token) #передаем информацию на сервер
    assert kit_response.status_code == 400 #проверяем код ответа

#Тест №11: Создание набора с другим типом данных в названии (число)
def test_11_create_kit_wrong_type_failed():
    negative_assert(123)
