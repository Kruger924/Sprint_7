"""Проверки для операций с курьерами"""


def check_courier_created(response_data: dict) -> None:
    """Проверка успешного создания курьера"""
    assert response_data.get("ok") is True


def check_courier_duplicate(response_json: dict) -> None:
    """Проверка ошибки при дублировании курьера"""
    assert response_json.get("message") == "Этот логин уже используется"


def check_courier_validation_error(response_json: dict) -> None:
    """Проверка ошибки валидации при создании курьера"""
    assert response_json.get("message") == "Недостаточно данных для создания учетной записи"
