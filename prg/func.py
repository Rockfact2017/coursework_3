import json
import datetime
import pathlib

# Получение текущего рабочего каталога
cwd = pathlib.Path.cwd()

# Загрузка данных из файла
with open(cwd / 'operations.json') as f:
    operations = json.load(f)

# Фильтрация выполненных операций
executed_operations = []
for operation in operations:
    if 'state' in operation and operation['state'] == 'EXECUTED':
        executed_operations.append(operation)

# Сортировка операции по дате в порядке убывания
executed_operations.sort(key=lambda operation: operation['date'], reverse=True)

# Вывод на экран последние 5 операций
for operation in executed_operations[:5]:
    # Преобразование даты в формат ДД.ММ.ГГГГ
    date = datetime.datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

    # Маскировка номера карты и счета
    from_masked = operation['from'][-4:] if 'from' in operation and operation['from'] else ''
    to_masked = operation['to'][-4:] if 'to' in operation and operation['to'] else ''

    # Вывод операции на экран
    print(f'{date} {operation["description"]}')
    if 'from' in operation and operation['from']:
        print(f'{" ".join(operation["from"].split()[1:])} **** **** **** {from_masked}')
    if 'to' in operation and operation['to']:
        print(f'Счет **** **** **** {to_masked}')
    print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}')
    print()
