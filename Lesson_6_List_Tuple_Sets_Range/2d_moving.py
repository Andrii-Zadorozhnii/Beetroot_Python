# 2D случайное блуждание.
# Двумерное случайное блуждание моделирует поведение частицы, движущейся по сетке точек.
# На каждом шаге случайный блуждающий движется на север, юг, восток или запад с вероятностью, равной 1/4, независимо от предыдущих движений.
# Напишите программу, которая принимает целочисленный аргумент командной строки n и оценивает, сколько времени потребуется случайному блуждающему, чтобы достичь границы квадрата размером 2n на 2n, центрированного в точке начала.
import random

pool_size = 2 * int(input('Please write n: '))

position = [0,0,0,0]

north = position[0]
south = position[1]
west = position[2]
east = position[3]

while max(position) <= pool_size:
    direction = random.randint(1, 4)
    # print(position)
    if direction == 1:
        north += 1
        south -= 1
        # print('Step to North')
    elif direction == 2:
        south += 1
        north -= 1
#         print('Step to South')

    elif direction == 3:
        west += 1
        east -= 1
        # print('Step to West')

    elif direction == 4:
        east += 1
        west -= 1
        # print('Step to East')

    position = [north, south, west, east]
    # position[random.randint(0,3)] += random.randint(-1,1)

print("Maximum position value:", max(position))
print(f'\nFinal position: \nNorth: {position[0]}\nSouth: {position[1]}\nWest: {position[2]}\nEast: {position[3]}')

