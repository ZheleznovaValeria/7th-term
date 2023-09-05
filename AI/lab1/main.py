import matplotlib.pyplot as plt
from random import randint, sample
import numpy as np
from math import sqrt


# функція, що генерує координати міст
def coordinates_for_cities(num_cities):
    X, Y = [], []
    for i in range(0, int(num_cities), 1):
        X.append(randint(0, 100))
        Y.append(randint(0, 100))
    return [X, Y]


# функія, що генерую початкову популяцію
def generate_individuals(population_size, num_cities):
    cities = []
    for i in range(1, int(num_cities)):
        cities.append(i)
    all_ways = []
    for i in range(population_size):
        temp = sample(cities, int(num_cities) - 1)
        temp.insert(0, 0)
        all_ways.append(temp)
    return all_ways


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def path_length(points, individual):
    path_length = 0
    for i in range(1, len(individual)):
        path_length = path_length + distance(points[0][individual[i - 1]], points[1][individual[i - 1]],
                                             points[0][individual[i]], points[0][individual[i]])
        if i == individual:
            path_length = path_length + distance(points[0][individual[0]], points[1][individual[0]],
                                                 points[0][individual[i]], points[0][individual[i]])
    return path_length




def choose_parents(population_size):
    parents = []
    temp = []
    for i in range(population_size * 2):
        temp.append(i)
    for i in range(population_size * 2):
        if i not in parents:
            parents.append(i)
            temp.remove(i)
            if len(temp) != 1:
                k = randint(0, len(temp) - 1)
                parents.append(temp[k])
                temp.remove(temp[k])
            else:
                parents.append(temp[0])
    return parents


def make_new_population(population):  # список родителей, список с путями
    new_population = []
    num_pop = len(population[0])
    parents = choose_parents(len(population))
    for i in range(0, len(parents) // 2 - 1, 2):
        slice_point1 = randint(1, num_pop - 3)
        slice_point2 = randint(slice_point1 + 1, num_pop - 2)
        ch1 = population[i][:slice_point1]
        ch2 = population[i + 1][:slice_point1]
        t1, t2 = population[i][slice_point2:], population[i + 1][slice_point2:]
        for j in range(num_pop):
            if (population[i][(j + slice_point1) % num_pop] not in ch2):
                if (population[i][(j + slice_point1) % num_pop] not in t2):
                    ch2.append(population[i][(j + slice_point1) % num_pop])

            if (population[i + 1][(j + slice_point1) % num_pop] not in ch1):
                if (population[i + 1][(j + slice_point1) % num_pop] not in t1):
                    ch1.append(population[i + 1][(j + slice_point1) % num_pop])

        ch1 = ch1 + population[i][slice_point2:]
        ch2 = ch2 + population[i + 1][slice_point2:]
        new_population.append(ch1)
        new_population.append(ch2)

    return new_population

def mutations(population, percent_mutation):
    count_mutation = (int(len(population)) * int(percent_mutation)) // 100
    for i in range(count_mutation):
        mut_population = randint(0, len(population) - 1)
        point1 = randint(0, len(population[0]) - 1)
        point2 = randint(0, len(population[0]) - 1)
        temp = population[mut_population][point1]
        population[mut_population][point1] = population[mut_population][point2]
        population[mut_population][point2] = temp
    return population


def delete_population(population_size, distances, population):
    delete_popul = population_size
    while delete_popul > population_size / 2:
        delete_popul = delete_popul - 1
        idx = distances.index(max(distances))
        distances.pop(idx)
        population.pop(idx)
    return population


# введення основних данних
print('Введіть кількість міст:')
num_cities = int(input())
print('Введіть кількість ітерацій:')
num_iter = int(input())
print('Введіть відсоток мутації:')
percent_mutation = int(input())
population_size = 28

positions = coordinates_for_cities(num_cities)
print('Координати міст =', positions)

population = generate_individuals(population_size, num_cities)
print('Згенерована популяція = ', population)

fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(np.array(positions[0]), np.array(positions[1]), c='black')

# прорахуємо дистанцію для кожної особини популяції
distances = []
for i in population:
    distances.append(round(path_length(positions, i), 3))
print('\nДовжина шляху для кожного варіанту', distances)
print('Мінімальна довжина шляху =', min(distances))
print()

iter = 1
while num_iter > 0:
    print('Ітерація = ', iter)
    iter = iter + 1
    num_iter = num_iter - 1

    # зробимо відбір половини популції
    population = delete_population(population_size, distances, population)

    population = population + make_new_population(population)

    population = mutations(population, percent_mutation)

    distances = []
    for i in population:
        distances.append(round(path_length(positions, i), 3))
    print('Довжина шляху для кожного варіанту після кросинговеру та мутації\n', distances)
    print('Мінімальна довжина шляху =', min(distances))
    idx = distances.index(max(distances))
    x, y = [], []
    for i in range(int(num_cities)):
        x.append(positions[0][population[idx][i]])
        y.append(positions[1][population[idx][i]])
    x.append(x[0])
    y.append(y[0])
    if num_iter != 0:
        ax.plot(x, y, color=np.random.rand(3, ), alpha=0.75)
    else:
        ax.plot(x, y, 'r', linewidth=4)
    print('------------------------------------------------------------------------------------------\n')

for i in range(0, int(num_cities), 1):
    ax.annotate(str(i), (positions[0][i] + 0.2, positions[1][i] + 0.2))
plt.show();