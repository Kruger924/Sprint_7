import allure
import pytest
import requests
from helps import DataCourier
from checks.courier_checks import check_courier_created, check_courier_duplicate, check_courier_validation_error
from data.endpoints import Endpoints
from data.urls import Urls


class TestCreateCourier:

    @allure.title('Проверка создания нового курьера')
    @allure.description('Отправка запроса на создание нового курьера, проверка ответа и удаление созданного курьера')
    def test_registration_courier_success(self, courier):
        courier_data = courier
        assert courier_data["status_code"] == 201
        check_courier_created(courier_data["response"])

    @allure.title('Проверка ошибки при дублировании курьера при создании')
    @allure.description('Отправка повторного запроса на создание курьера, проверка ответа и удаление курьера')
    @allure.step('Повторная регистрация курьера (ожидаем ошибку 409)')
    def test_registration_double_courier_failed(self, courier):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])
        assert response.status_code == 409
        check_courier_duplicate(response.json())

    @allure.title('Проверка ошибки при создании курьера без заполнения обязательных полей Login Password')
    @allure.description('Отправка запроса на создание курьера без заполнения обязательных полей Login Password и проверка ответа')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    @allure.step('Регистрация курьера без обязательных полей (ожидаем ошибку 400)')
    def test_courier_registration_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        check_courier_validation_error(response.json())