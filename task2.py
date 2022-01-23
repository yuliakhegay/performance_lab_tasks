import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_path1', metavar='path1', type=str, help='Enter the path of file 1')
parser.add_argument('file_path2', metavar='path2', type=str, help='Enter the path of file 2')
args = parser.parse_args()

file_path1 = args.file_path1
file_path2 = args.file_path2


def get_point_location(path1, path2):
    """Определяет положение точки относительно окружности
       0: на окружности
       1: внутри
       2: снаружи"""
    with open(path1, 'r', encoding='utf8') as file1:
        x1, y1, r = (float(x) for x in file1.read().split())

    with open(path2, 'r', encoding='utf8') as file2:
        for line in file2:
            x2, y2 = (float(x) for x in line.split())
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if dist < r:
                loc = 1
            elif dist > r:
                loc = 2
            else:
                loc = 0
            yield loc


for elem in get_point_location(file_path1, file_path2):
    print(elem)
