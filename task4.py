import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', metavar='path', type=str, help='Enter the path of the file with a list of numbers')
args = parser.parse_args()

path = args.path


def get_steps(ind, nums):
    """Вычисляет кол-во шагов для приведения всех чисел к числу с индексом ind"""
    steps = 0
    for j in range(len(nums)):
        steps += abs(nums[ind] - nums[j])
    return steps


def min_steps(file_path):
    """Вычисляет минимальное кол-во шагов, нужных для приведения всех чисел к одному"""
    with open(file_path, 'r', encoding='utf8') as file:
        nums = [int(x) for x in file.read().split()]

    # Считаем, сколько шагов требуется, чтобы привести все числа к каждому числу в массиве
    minim = get_steps(0, nums)
    for i in range(1, len(nums)):
        steps_cnt = get_steps(i, nums)
        if steps_cnt < minim:
            minim = steps_cnt

    return minim


print(min_steps(path))
