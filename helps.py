from faker import Faker 
import requests
import allure

from data.endpoints import Endpoints
from data.urls import Urls
from data.test_data import (
    ORDER_DATA,
    INVALID_DATA_LOGIN_WITHOUT_LOGIN,
    INVALID_DATA_LOGIN_WITHOUT_PASSWORD,
    NULL_DATA_LOGIN,
    INCORRECT_DATA_LOGIN,
)


class DataOrder:
    """Класс для доступа к данным заказа."""
    data = ORDER_DATA


class DataCourier:
    """Класс для доступа к данным курьера."""
    invalid_data_login_without_login = INVALID_DATA_LOGIN_WITHOUT_LOGIN
    invalid_data_login_without_password = INVALID_DATA_LOGIN_WITHOUT_PASSWORD
    null_data_login = NULL_DATA_LOGIN
    incorrect_data_login = INCORRECT_DATA_LOGIN


class CourierDataGenerator:
    """Генерация фейковых данных для тестов курьеров."""

    @staticmethod
    def generate_valid_courier_data() -> dict:
        """Генерация валидных данных для создания курьера."""
        fake = Faker("ru_RU")
        return {
            "login": fake.user_name(),
            "firstName": fake.first_name(),
            "password": fake.password()
        }

    @staticmethod
    def generate_invalid_courier_data_without_login() -> dict:
        """Генерация невалидных данных без логина."""
        fake = Faker("ru_RU")
        return {
            "login": "",
            "firstName": fake.first_name(),
            "password": fake.password()
        }

    @staticmethod
    def generate_invalid_courier_data_without_password() -> dict:
        """Генерация невалидных данных без пароля."""
        fake = Faker("ru_RU")
        return {
            "login": fake.user_name(),
            "password": "",
            "firstName": fake.first_name()
        }


class Courier:

    # функция регистрации в системе с возвратом ответа и данных курьера
    @staticmethod
    @allure.step('Регистрация курьера в системе')
    def courier_registration_in_the_system_and_get_courier_data():
        data = CourierDataGenerator.generate_valid_courier_data()
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=data)
        return {"response": response.json(), "status_code": response.status_code, "data": data}

    # функция логина в системе с возвратом ответа и id курьера
    @staticmethod
    @allure.step('Логин курьера в системе')
    def courier_login_in_the_system_and_get_id_courier(data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}', data=data)
        return {"id": str(response.json()["id"]), "response": response.json(), "status_code": response.status_code}

    # функция удаления курьера
    @staticmethod
    @allure.step('Удаление курьера из системы')
    def courier_subsequent_deletion(id):
        response = requests.delete(f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{id}')
        return {"response": response.json(), "status_code": response.status_code}

