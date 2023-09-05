import sys
import math
import os
from os.path import isfile
import numpy as np

teach_dir = os.path.expanduser('D:/teach')
train_path = os.path.expanduser('D:/train/train.txt')

SHAPE_SIDE = 7  # кількість біт в стороні образа
dict = {'-': -1, '1': 1}  # словник для відображення образів у вихідному форматі
shapes = []  # образи.якими в мійбутньому буде навчена мережа
neurons = int(math.pow(SHAPE_SIDE, 2))  # кількість нейронів
W = []  # матриця ваговіх коефіцієнтів розмірності 49х49 та заповнення нулями
for i in range(neurons):
    W.append([0 for x in range(neurons)])
teach_shapes = []  # образи, якими було проведено навчання

'''
Створення списку файлів в директорії
'''


def parse(dir):
    shapes_files = []
    for filename in os.listdir(dir):
        path = os.path.join(dir, filename)
        if isfile(path):
            shapes_files.append(path)

    for path in shapes_files:
        shape = parse_shape(path)
        shapes.append(shape)
    return shapes


'''
Зчитування фалу та збереження фігури у вигляді списку
'''


def parse_shape(path):
    with open(path) as f:
        contents = f.read()
        contents = contents.replace("\n", "")
        contents = contents.replace("\r", "")
        shape = []
        for c in contents:
            shape.append(dict[c])
        return shape


'''
відображення образів
'''


def printshape(obraz, size):
    for i in range(0, len(obraz), size):
        row = ''
        for j in obraz[i:i + size]:
            row += list(dict.keys())[list(dict.values()).index(j)]
        print(row)


'''
навчання мережі
'''


def teach(shape):
    teach_shapes.append(shape)
    X = shape
    for i in range(0, SHAPE_SIDE ** 2, 1):
        for j in range(0, SHAPE_SIDE ** 2, 1):
            if (i == j):
                W[i][j] = 0
            else:
                W[i][j] += X[i] * X[j]


'''
функція активації
'''


def function(x):
    for i in range(SHAPE_SIDE ** 2):
        if x[i][0] >= 0:
            x[i][0] = 1
        else:
            x[i][0] = -1
    return x


"""
функція для розпізнавання образів, тренування мережі
"""


def recognize(shape):
    Y = function(np.dot(W, shape.reshape(SHAPE_SIDE ** 2, 1)))
    for i in range(50):
        Y = function(np.dot(W, Y))
    return Y


"""
перевірка матриці вагів на симетричність
"""


def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)


"""
main
"""
shapes = parse(teach_dir)
shape = parse_shape(train_path)

print("Letters for learn:")
for o in shapes:
    printshape(o, SHAPE_SIDE)
    print()

print("Learning:")
for o in shapes:
    teach(o)
print()

W = np.array(W)
shape = np.array(shape)

print('Is the matrix W symmetrical?')
print(check_symmetric(W, 1e-8), '\n')

print('Training:')
print("Train shape:")
printshape(shape, SHAPE_SIDE)
print()

print('Recognition shape:')
recshape = recognize(shape)

printshape(recshape, SHAPE_SIDE)
