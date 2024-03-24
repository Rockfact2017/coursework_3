import json
import os
from datetime import datetime

import pytest

from prg.utils import sorting_operations


# Тест для функции read_file
def test_read_file():
    """Тест проверяет, что функция read_file правильно читает данные из файла"""
    # Указываем путь к тестовому файлу
    file_path = "tests/data/test_data.json"

    # Создаем ожидаемые данные
    expected_data = [
        {
            "date": "2023-03-15T12:34:56.789Z",
            "state": "EXECUTED",
            "from": "Счет RU12345678901234567890",
            "to": "Карта 1234567890123456",
            "operationAmount": {
                "amount": 1000.00,
                "currency": {
                    "name": "RUB"
                }
            }
        },
        {
            "date": "2023-03-14T11:22:33.456Z",
            "state": "CANCELED",
            "from": "Счет RU98765432109876543210",
            "to": "Карта 9876543210987654",
            "operationAmount": {
                "amount": 2000.00,
                "currency": {
                    "name": "USD"
                }
            }
        },
        {
            "date": "2023-03-13T10:11:22.567Z",
            "state": "EXECUTED",
            "from": "Карта 1122334455667788",
            "to": "Счет RU1122334455667788",
            "operationAmount": {
                "amount": 3000.00,
                "currency": {
                    "name": "EUR"
                }
            }
        }
    ]

    # Вызываем функцию read_file и проверяем, что она вернула ожидаемые данные
    assert sorting_operations.read_file(file_path) == expected_data


# Тест для функции sorting_operations
def test_sorting_operations():
    """Тест проверяет, что функция sorting_operations правильно сортирует операции"""
    # Указываем путь к тестовому файлу
    file_path = "tests/data/test_data.json"

    # Создаем ожидаемые отсортированные данные
    expected_sorted_data = [
        {
            "date": "2023-03-15T12:34:56.789Z",
            "state": "EXECUTED",
            "from": "Счет RU12345678901234567890",
            "to": "Карта 1234567890123456",
            "operationAmount": {
                "amount": 1000.00,
                "currency": {
                    "name": "RUB"
                }
            }
        },
        {
            "date": "2023-03-13T10:11:22.567Z",
            "state": "EXECUTED",
            "from": "Карта 1122334455667788",
            "to": "Счет RU1122334455667788",
            "operationAmount": {
                "amount": 3000.00,
                "currency": {
                    "name": "EUR"
                }
            }
        }
    ]

    # Вызываем функцию sorting_operations и проверяем, что она вернула ожидаемые отсортированные данные
    assert sorting_operations.sorting_operations(file_path) == expected_sorted_data
