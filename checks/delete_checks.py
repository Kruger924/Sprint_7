"""Проверки для операций удаления курьеров"""


def check_courier_deleted(response_json: dict) -> None:
    """Проверка успешного удаления курьера"""
    assert response_json.get("ok") is True


def check_delete_not_found(response_json: dict) -> None:
    """Проверка ошибки при удалении несуществующего курьера"""
    assert response_json.get("message") == "Курьера с таким id нет"

def check_delete_error_id(response_json: dict) -> None:
    """Проверка ошибки при удалении курьера без указания id"""
    assert response_json.get("message") == "Недостаточно данных для удаления курьера"