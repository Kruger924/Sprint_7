"""Проверки для операций с заказами"""


def check_order_created(response_json: dict) -> None:
    """Проверка успешного создания заказа"""
    assert "track" in response_json


def check_order_list(response_json: dict) -> None:
    """Проверка получения списка заказов"""
    assert "track" in str(response_json)
