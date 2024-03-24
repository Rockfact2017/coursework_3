import json
from datetime import datetime


def read_file(file_path: str) -> list:
    """Считывает json данные по транзакциям и возвращает список словарей"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sorting_operations(file_path):
    """Возвращает отсортированный по датам список успешных транзакций"""
    all_info = read_file(file_path)
    new_list = []
    for change_date in all_info:
        if not change_date or change_date["state"] == "CANCELED":
            continue
        elif change_date["state"] == 'EXECUTED':
            new_list.append(change_date)

    new_list.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return new_list
import json
from datetime import datetime


def read_file(file_path: str) -> list:
    """Считывает json данные по транзакциям и возвращает список словарей"""
    # Открываем файл с данными о транзакциях
    with open(file_path, 'r', encoding='utf-8') as file:
        # Считываем данные из файла
        data = json.load(file)
    # Возвращаем список словарей с данными о транзакциях
    return data


def sorting_operations(file_path):
    """Возвращает отсортированный по датам список успешных транзакций"""
    # Считываем данные о транзакциях из файла
    all_info = read_file(file_path)
    # Создаем новый список для успешных транзакций
    new_list = []
    # Перебираем все транзакции
    for change_date in all_info:
        # Пропускаем пустые транзакции и транзакции в состоянии "CANCELED"
        if not change_date or change_date["state"] == "CANCELED":
            continue
        # Добавляем в новый список только успешные транзакции
        elif change_date["state"] == 'EXECUTED':
            new_list.append(change_date)

    # Сортируем транзакции по дате в обратном порядке (от новых к старым)
    new_list.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    # Возвращаем отсортированный список успешных транзакций
    return new_list



