import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('tests_path', metavar='tests_path', type=str, help='Enter the path of the tests file')
parser.add_argument('values_path', metavar='values_path', type=str, help='Enter the path of the values file')
args = parser.parse_args()

tests_path = args.tests_path
values_path = args.values_path


def fill_values(tests_lst, values_dct):
    """Заполняет поля value в структуре tests.json"""
    for test_dct in tests_lst:
        for k, v in test_dct.items():
            if k == 'id' and values_dct.get(v):
                test_dct.update(values_dct[v])  # заполнить поле value на основе значения id
            elif type(v) == list:   # проверка вложенности
                fill_values(v, values_dct)
    return tests_lst


def make_report(path1, path2):
    """Формирует файл report.json c заполненными полями value в структуре tests.json"""
    with open(path1, 'r', encoding='utf8') as tests_file, \
            open(path2, 'r', encoding='utf8') as values_file:
        tests = json.load(tests_file)
        values = json.load(values_file)

    # создать словарь вида 'значение id: исходный словарь'
    values_dct = {dct['id']: dct for dct in values['values']}

    fill_values(tests['tests'], values_dct)

    with open('report.json', 'w', encoding='utf8') as output:
        json.dump(tests, output, indent=2)


make_report(tests_path, values_path)
