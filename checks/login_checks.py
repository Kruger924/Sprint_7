"""Проверки для операций логина курьеров"""


def check_courier_logged_in(response_json: dict) -> None:
    """Проверка успешной авторизации курьера"""
    assert "id" in response_json


def check_login_validation_error(response_json: dict) -> None:
    """Проверка ошибки валидации при авторизации с недостаточным количеством данных для входа."""
    assert response_json.get("message") == "Недостаточно данных для входа"


def check_login_not_found(response_json: dict) -> None:
    """Проверка ошибки авторизации при попытке ввода данных несуществующего курьера."""
    assert response_json.get("message") == "Учетная запись не найдена"
