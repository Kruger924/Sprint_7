import json
import allure
import pytest
import requests
from helps import DataOrder
from data.endpoints import Endpoints
from data.urls import Urls


class TestOrderCreate:

    @allure.title('Проверка оформления заказа с различными цветами самоката')
    @allure.description('Отправка запроса на создание заказа с поочередным добавлением различных цветов и проверка ответа')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order_success(self, color):
        headers = {"Content-type": "application/json"}
        data = DataOrder.data
        data.update(color)
        data = json.dumps(data)
        response = requests.post(f'{Urls.QA_SCOOTER_URL}{Endpoints.create_order}', headers=headers, data=data)
        assert response.status_code == 201
        assert "track" in response.text