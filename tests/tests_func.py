import json
import datetime
import pytest

def test_load_operations():
    with open('/Users/artem/PycharmProjects/coursework_3/prg/operations.json') as f:
        operations = json.load(f)
    assert isinstance(operations, list)
    assert len(operations) > 0

def test_filter_executed_operations():
    operations = [
        {'state': 'EXECUTED', 'date': '2023-03-08T12:34:56.789Z'},
        {'state': 'NEW', 'date': '2023-03-07T11:22:33.456Z'},
        {'state': 'EXECUTED', 'date': '2023-03-06T10:11:22.345Z'},
    ]
    executed_operations = filter_executed_operations(operations)
    assert isinstance(executed_operations, list)
    assert len(executed_operations) == 2
    assert executed_operations[0]['date'] == '2023-03-08T12:34:56.789Z'
    assert executed_operations[1]['date'] == '2023-03-06T10:11:22.345Z'

def test_sort_operations_by_date():
    operations = [
        {'state': 'EXECUTED', 'date': '2023-03-08T12:34:56.789Z'},
        {'state': 'EXECUTED', 'date': '2023-03-06T10:11:22.345Z'},
        {'state': 'EXECUTED', 'date': '2023-03-07T11:22:33.456Z'},
    ]
    sorted_operations = sort_operations_by_date(operations)
    assert isinstance(sorted_operations, list)
    assert len(sorted_operations) == 3
    assert sorted_operations[0]['date'] == '2023-03-08T12:34:56.789Z'
    assert sorted_operations[1]['date'] == '2023-03-07T11:22:33.456Z'
    assert sorted_operations[2]['date'] == '2023-03-06T10:11:22.345Z'

def test_format_date():
    date = '2023-03-08T12:34:56.789Z'
    formatted_date = format_date(date)
    assert isinstance(formatted_date, str)
    assert formatted_date == '08.03.2023'

def test_mask_number():
    number = '1234567890123456'
    masked_number = mask_number(number)
    assert isinstance(masked_number, str)
    assert masked_number == 'XXXX XX** **** XXXX'

def test_print_operation():
    operation = {
        'date': '2023-03-08T12:34:56.789Z',
        'description': 'Перевод на карту ****1234',
        'from': '1234567890123456',
        'to': '9876543210987654',
        'operationAmount': {
            'amount': '1000.00',
            'currency': {
                'name': 'RUB'
            }
        }
    }
    print_operation(operation)
    # Проверка вывода операции на экран с помощью захвата вывода
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        print_operation(operation)
    output = captured.getvalue()
    assert '08.03.2023 Перевод на карту ****1234' in output
    assert 'XXXX XX** **** XXXX -> **XXXX' in output
    assert '1000.00 RUB' in output

def test_main():
    # Проверка вывода на экран последних 5 выполненных операций
    with contextlib.redirect_stdout(io.StringIO()) as f:
        main()
    output = f.getvalue()
    assert len(output.splitlines()) > 5

