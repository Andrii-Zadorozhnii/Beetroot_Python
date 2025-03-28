# 2D случайное блуждание.
# Двумерное случайное блуждание моделирует поведение частицы, движущейся по сетке точек.
# На каждом шаге случайный блуждающий движется на север, юг, восток или запад с вероятностью, равной 1/4, независимо от предыдущих движений.
# Напишите программу, которая принимает целочисленный аргумент командной строки n и оценивает, сколько времени потребуется случайному блуждающему, чтобы достичь границы квадрата размером 2n на 2n, центрированного в точке начала.

import random


pool_size = 2 * int(input('Please write n: '))
print(
    f'Pool size is: {pool_size}'
)

x, y = (0,0)
steps = 0
print(
    f'Initial position is: x:{x}, y:{y}'
)


# Loop to adjust positions until one of them exceeds pool_size
while x < pool_size and y < pool_size:
    direction = random.randint(1, 4)
    # Update positions based on the random direction
    if direction == 1:
        x += 1
    elif direction == 2:
        x -= 1
    elif direction == 3:
        y += 1
    elif direction == 4:
        y -= 1
    print(
        f'Position is: x:{x}, y:{y}'
    )
    steps += 1


print(
    f'Steps for completion: {steps}'
)
print(
    f'Final position is: x:{x}, y:{y}'
)