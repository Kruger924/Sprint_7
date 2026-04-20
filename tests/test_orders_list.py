import allure
import requests
from data.endpoints import Endpoints
from data.urls import Urls


class TestOrdersList:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Получение списка заказов и проверка ответа')
    @allure.step('Получение списка заказов')
    def test_list_orders_success(self):
        response = requests.get(f'{Urls.QA_SCOOTER_URL}{Endpoints.get_orders_list}')
        assert response.status_code == 200
        assert "track" in response.text