# Sprint_7
Sprint_7_Kulikov_S_P
Проект на тему "Тестирование API".
В данном проекте представлены автотесты для сервиса Яндекс.Самокат (https://qa-scooter.praktikum-services.ru/).

# Список файлов:
allure_results - каталог с отчетом о тестировании
tests/ - каталог с автотестами
tests/test_create_courier.py - файл с проверками создания курьера
tests/test_login_courier.py - файл с проверками авторизации курьера
tests/test_order.py - файл с проверками создания заказа
tests/test_orders_list.py - файл с проверками получения списков заказа
data/ - каталог с данными для тестирования
data/endpoints.py - файл с эндпоинтами
data/urls - файл с URL
helps.py - данные со вспомогательными данными для тестирования
requirements.txt - файл с внешними зависимостями
conftest.py - файл с фикстурой

# Перед работой необходимо установить зависимости, выполнив команду:
pip install -r requirements.txt

# Запуск тестов:
pytest tests --alluredir=allure_results

# Просмотр отчета:
allure serve allure_results