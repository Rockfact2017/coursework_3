import pytest

from datetime import datetime

from config import DIR_JSON
from prg.utils import sorting_operations


# Тест для функции get_correct_date
def test_get_correct_date():
    """Тест проверяет, что функция get_correct_date правильно преобразует дату в строку"""
    # Проверяем, что функция возвращает правильную дату для даты в формате ISO 8601
    assert get_correct_date("2023-03-15T12:34:56.789Z") == "15.03.2023"


# Тест для функции format_payment
def test_format_payment_with_account_number():
    """Тест проверяет, что функция format_payment правильно форматирует номер счета"""
    # Проверяем, что функция возвращает правильный отформатированный номер счета
    assert format_payment("Счет RU12345678901234567890") == "RU12345678901234567890**"


def test_format_payment_with_card_number():
    """Тест проверяет, что функция format_payment правильно форматирует номер карты"""
    # Проверяем, что функция возвращает правильный отформатированный номер карты
    assert format_payment("Карта 1234567890123456") == "1234 56** **** 1234"


def test_format_payment_with_no_data():
    """Тест проверяет, что функция format_payment возвращает правильное значение для пустых данных"""
    # Проверяем, что функция возвращает "Данные отсутсвуют" для пустых данных
    assert format_payment(None) == "Данные отсутсвуют"


# Тест для функции operations_print
def test_operations_print():
    """Тест проверяет, что функция operations_print правильно выводит отсортированные операции"""
    # Создаем ожидаемый вывод
    expected_output = """

15.03.2023 Перевод организации
Счет RU12345678901234567890** -> Карта 1234 56** **** 1234
1000.00 RUB"""

    # Перенаправляем вывод функции в буфер
    with pytest.capture_stdout() as out:
        operations_print()

    # Проверяем, что ожидаемый вывод содержится в выводе функции
    assert expected_output in out.getvalue()
