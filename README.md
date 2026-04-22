# Sprint_7
Sprint_7_Kulikov_S_P
Проект на тему "Тестирование API".
В данном проекте представлены автотесты для сервиса Яндекс.Самокат (https://qa-scooter.praktikum-services.ru/).

# Список файлов:
*allure_results/ - каталог с отчетом о тестировании
*tests/ - каталог с автотестами
*tests/test_create_courier.py - файл с проверками создания курьера
*tests/test_login_courier.py - файл с проверками авторизации курьера
*tests/test_order.py - файл с проверками создания заказа
*tests/test_orders_list.py - файл с проверками получения списка заказов
*tests/test_delete_courier.py - файл с проверками удаления курьера
*checks/ - каталог с логическими методами и проверками
*checks/courier_checks.py - файл с проверками для операций с курьерами
*checks/login_checks.py - файл с проверками для операций авторизации курьеров
*checks/order_checks.py - файл с проверками для операций с заказами
*checks/delete_checks.py - файл с проверками для операций удаления курьеров
*data/ - каталог со статичными данными для тестирования
*data/endpoints.py - файл с эндпоинтами API
*data/urls.py - файл с базовым URL
*data/test_data.py - файл с тестовыми данными
*helps.py - вспомогательные функции
*conftest.py - файл с фикстурами
*requirements.txt - файл с внешними зависимостями
*README.md - документация проекта

# Перед работой необходимо установить зависимости, выполнив команду:
pip install -r requirements.txt

# Запуск тестов:
pytest tests --alluredir=allure_results

# Просмотр отчета:
allure serve allure_results