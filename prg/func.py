from datetime import datetime

from config import DIR_JSON
from prg.utils import sorting_operations

def get_correct_date(new_date):
    """Функция возвращает коректную дату в соответствии с ТЗ"""
    # Преобразуем строку с датой в объект datetime
    date_new = datetime.fromisoformat(new_date)
    # Форматируем дату в соответствии с ТЗ
    return datetime.strftime(date_new, "%d.%m.%Y")


def format_payment(info_payment):
    """Принимает счет и форматирует"""
    if info_payment:
        # Разбиваем строку с информацией о счете на список слов
        account = info_payment.split()
        # Если строка начинается с "Счет", то это счет отправителя
        if info_payment.startswith("Счет"):
            # Берем последние 4 символа номера счета
            account_alpha = account.pop()
            account_alpha = f"**{account_alpha[-4:]}"
            # Добавляем отформатированный номер счета в список
            account.append(account_alpha)
        # Иначе это счет получателя
        else:
            # Берем первые 4 символа и последние 4 символа номера счета
            account_alpha = account.pop()
            account_alpha = f"{account_alpha[0:4]} {account_alpha[4:6]}** **** {account_alpha[-4:]}"
            # Добавляем отформатированный номер счета в список
            account.append(account_alpha)
        # Возвращаем отформатированную строку с информацией о счете
        return " ".join(account)
    # Если информация о счете отсутствует, возвращаем сообщение об этом
    return "Данные отсутсвуют"


def operations_print():
    # Получаем список отсортированных транзакций
    sorted_operations = sorting_operations(DIR_JSON)
    # Выводим первые 5 транзакций
    for item in sorted_operations[:5]:
        # Выводим дату транзакции
        print(f'\n{get_correct_date(item["date"])} Перевод организации')
        # Выводим отформатированные счета отправителя и получателя
        print(f'{format_payment(item.get("from"))} -> {format_payment(item["to"])}')
        # Выводим сумму и валюту транзакции
        print(f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')
