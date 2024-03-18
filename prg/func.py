import json
import datetime

# Загрузка данных из файла
with open('/Users/artem/PycharmProjects/coursework_3/prg/operations.json') as f:
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
    from_masked = 'XXXX XX** **** XXXX' if 'from' in operation and operation['from'] else ''
    to_masked = '**XXXX' if 'to' in operation and operation['to'] else ''

    # Вывод операции на экран
    print(f'{date} {operation["description"]}')
    print(f'{from_masked} -> {to_masked}')
    print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}')
    print()