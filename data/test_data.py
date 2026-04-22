# Статичные данные для тестов

# Данные для заказа самоката
ORDER_DATA = {
    "firstName": "Сергей",
    "lastName": "Куликов",
    "address": "г.Москва",
    "metroStation": 4,
    "phone": "+7 999 888 7654",
    "rentTime": 4,
    "deliveryDate": "2026-04-20",
    "comment": "Хочу быстрее кататься!",
}

# Некорректные данные для регистрации курьера без указания логина
INVALID_DATA_LOGIN_WITHOUT_LOGIN = {
    "login": "",
    "firstName": "Сергей",
    "password": "Куликов123"
}

# Некорректные данные для регистрации курьера без указания пароля
INVALID_DATA_LOGIN_WITHOUT_PASSWORD = {
    "login": "test",
    "password": "",
    "firstName": "Сергей"
}

# Данные несуществующего курьера
NULL_DATA_LOGIN = {
    "login": "test",
    "password": "test"
}

# Данные с невалидными значениями
INCORRECT_DATA_LOGIN = {
    "login": 12345,
    "password": True
}
