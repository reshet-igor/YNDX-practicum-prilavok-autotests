import sender_stand_request
import data


#  Вызываем функцию post_new_user в файле sender_stand_request.py и извлекаем из ответа сервера
#  токен нового пользователя, используюя ключ 'authToken'.
response = sender_stand_request.post_new_user(data.user_body)
auth_token = response.json()['authToken']


#  Функция создает копию словаря data.kit_body, сохраняя оригинальный словарь data.kit_body неизменным,
#  заменяет значение ключа "name" на значение name и возвращает этот новый словарь.
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


#  Получаем тело запроса kit_body, содержащее данные для создания нового набора.
#  Вызываем функцию post_new_client_kit в файле sender_stand_request.py и передаем тело запроса
#  kit_body и токен аутентификации auth_token.
#  Проверяем, что код ответа сервера равен 201.
#  Проверяем, что поле name в ответе совпадает с полем name в запросе.
def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201

    assert kit_response.json()["name"] == name


#  Получаем тело запроса kit_body, содержащее данные для создания нового набора.
#  Вызываем функцию post_new_client_kit в файле sender_stand_request.py и передаем тело запроса
#  kit_body и токен аутентификации auth_token.
#  Проверяем, что код ответа сервера равен 400.
def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400


#  Тест проверяет, что при значении name из 1 символа код ответа сервера равен 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


#  Тест проверяет, что при значении name из 511 символов код ответа — 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabc")


#  Тест проверяет, что при пустом значении name код ответа сервера равен 400.
def test_create_kit_empty_name_get_success_response():
    negative_assert_symbol("")


#  Тест проверяет, что при значении name из 512 символов код ответа сервера равен 400
def test_create_kit_512_letters_in_name_get_success_response():
    negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcda\
bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
dabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
cdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
abcdabcdabcdabcdabcdabcdabcdabcdabcdabAbcdabcdabcdabcdabcd")


#  Тест проверяет, что при значении name, состоящем из английских букв, код ответа сервера равен 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


#  Тест проверяет, что при значении name, состоящем из русских букв, код ответа сервера равен 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


#  Тест проверяет, что при значении name, состоящем из спецсимволов, код ответа сервера равен 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")


#  Тест проверяет, что при значении name, содержащем пробелы, код ответа сервера равен 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


#  Тест проверяет, что при значении name, состоящем из цифр, код ответа сервера равен 201,
#  в ответе поле name совпадает с полем name в запросе.
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")


#  Создаем тело комплекта путем копирования исходного тела из переменной "data.kit_body".
#  Из созданной переменной удаляем ключ "name".
#  Отправляем запрос на создание нового набора с использованием созданного тела и токена аутентификации.
#  Выполняем проверку, что код статуса ответа сервера равен 400.
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400


#  Тест проверяет, что при значении name, состоящем из другого типа данных (число), код ответа сервера равен 400.
def test_create_kit_intejer_in_name_get_success_response():
    negative_assert_symbol(123)