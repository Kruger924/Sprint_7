from faker import Faker 
import requests
import allure

from data.endpoints import Endpoints
from data.urls import Urls


class DataOrder:
    # данные для заказа самоката без цвета
    data = {
        "firstName": "Сергей",
        "lastName": "Куликов",
        "address": "г.Москва",
        "metroStation": 4,
        "phone": "+7 999 888 7654",
        "rentTime": 4,
        "deliveryDate": "2026-04-20",
        "comment": "Хочу быстрее кататься!",
    }

class DataCreateCourier:
    # функция генерации фэйковых валидных данных
    @staticmethod
    def generating_fake_valid_data_to_create_courier():
        fake = Faker("ru_RU")
        login = fake.user_name()
        password = fake.password()
        firstname = fake.first_name()
        data = {
            "login": login,
            "firstName": firstname,
            "password": password
        }

        return data

    # функция генерации фэйковых данных без поля "Login"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_login_field():
        fake = Faker("ru_RU")
        firstname = fake.first_name()
        password = fake.password()
        data = {
            "login": "",
            "firstName": firstname,
            "password": password
        }

        return data

    # функция генерации фэйковых данных без поля "Password"
    @staticmethod
    def generating_fake_invalid_data_to_create_courier_without_password_field():
        fake = Faker("ru_RU")
        login = fake.user_name()
        firstname = fake.first_name()
        data = {
            "login": login,
            "password": "",
            "firstName": firstname
        }

        return data


class DataCourier:
    # валидные данные для регистрации
    valid_data_login = DataCreateCourier.generating_fake_valid_data_to_create_courier()

    # невалидные данные для регистрации без поля "Login"
    invalid_data_login_without_login = DataCreateCourier.generating_fake_invalid_data_to_create_courier_without_login_field()

    # невалидные данные для регистрации без поля "Password"
    invalid_data_login_without_password = DataCreateCourier.generating_fake_invalid_data_to_create_courier_without_password_field()

    # данные несуществующего курьера
    null_data_login = {
        "login": "test",
        "password": "test"
    }

    # данные несуществующего курьера с невалидными значениями
    incorrect_data_login = {
        "login": 12345,
        "password": True
    }


class Courier:

    # функция регистрации в системе с возвратом ответа и данных курьера
    @staticmethod
    @allure.step('Регистрация курьера в системе')
    def courier_registration_in_the_system_and_get_courier_data():
        data = DataCreateCourier.generating_fake_valid_data_to_create_courier()
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    # функция логина в системе с возвратом ответа и id курьера
    @staticmethod
    @allure.step('Логин курьера в системе')
    def courier_login_in_the_system_and_get_id_courier(data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    # функция удаления курьера
    @staticmethod
    @allure.step('Удаление курьера из системы')
    def courier_subsequent_deletion(id):
        response = requests.delete(f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{id}')
        return {"response_text": response.text, "status_code": response.status_code}

