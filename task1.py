import argparse
from itertools import cycle

parser = argparse.ArgumentParser()
parser.add_argument('num1', metavar='n', type=int, help='maximum number of the array')
parser.add_argument('num2', metavar='m', type=int, help='interval length')
args = parser.parse_args()

num1 = args.num1
num2 = args.num2


def get_path(n, m):
    """Получает путь, где концом последнего интервала является первый элемент массива"""
    cycle_iter = cycle(x for x in range(1, n + 1))  # создание кругового массива
    path = []

    i = 0
    for elem in cycle_iter:
        i += 1
        if i == m and elem != 1:
            i = 1       # начать новый интервал
        if i == 1:
            path.append(elem)       # добавить первый элемент интервала в путь
        elif i == m and elem == 1:
            break

    return ''.join(str(elem) for elem in path)


print(get_path(num1, num2))
