import allure
import pytest
import requests
from helps import DataCourier
from data.endpoints import Endpoints
from data.urls import Urls


class TestCreateCourier:

    @allure.title('Проверка создания нового курьера')
    @allure.description('Отправка запроса на создание нового курьера, проверка ответа и удаление созданного курьера')
    def test_registration_courier_success(self, courier):
        courier_data = courier
        assert courier_data["status_code"] == 201
        assert courier_data["response_text"] == '{"ok":true}'

    @allure.title('Проверка ошибки при дублировании курьера при создании')
    @allure.description('Отправка повторного запроса на создание курьера, проверка ответа и удаление курьера')
    @allure.step('Повторная регистрация курьера (ожидаем ошибку 409)')
    def test_registration_double_courier_failed(self, courier):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier["data"])
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title('Проверка ошибки при создании курьера без заполнения обязательных полей Login Password')
    @allure.description('Отправка запроса на создание курьера без заполнения обязательных полей Login Password и проверка ответа')
    @pytest.mark.parametrize('courier_data', [DataCourier.invalid_data_login_without_login,
                                           DataCourier.invalid_data_login_without_password])
    @allure.step('Регистрация курьера без обязательных полей (ожидаем ошибку 400)')
    def test_courier_registration_without_parameters_failed(self, courier_data):
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}', data=courier_data)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text