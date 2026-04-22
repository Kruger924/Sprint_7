import allure
from helps import Courier
from checks.delete_checks import check_courier_deleted, check_delete_not_found, check_delete_error_id


class TestDeleteCourier:

    @allure.title('Проверка удаления курьера')
    @allure.description('Отправа запроса на удаление курьера и проверка ответа')
    def test_delete_courier_success(self, courier_delete):
        courier_id = courier_delete
        response = Courier().courier_subsequent_deletion(courier_id["id"])
        assert response["status_code"] == 200
        check_courier_deleted(response["response"])


    @allure.title('Проверка удаления курьера с несуществующим ID')
    @allure.description('Отправка запроса на удаление курьера с несуществующим ID и проверка ответа')
    def test_delete_courier_invalid_id_failed(self):
        courier_id = '123456'
        response = Courier().courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 404
        check_delete_not_found(response["response"])

    @allure.title('Проверка удаления курьера без ID')
    @allure.description('Отправка запроса на удаление курьера без ID и проверка ответа')
    def test_delete_courier_none_id_failed(self):
        courier_id = ''
        response = Courier().courier_subsequent_deletion(courier_id)
        assert response["status_code"] == 400
        check_delete_error_id(response["response"])