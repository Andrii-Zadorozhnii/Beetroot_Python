# Task 1
#
# The greatest number
#
# Write a Python program to get the largest number from a list of random numbers with the length of 10
#
# Constraints: use only while loop and random module to generate numbers

import random

random_list = []


while len(random_list) <= 9:
    random_list.append(random.randint(1,11))

print('\tTask 1\n')
print(f'Random number list: {random_list}\n')

# Task 2
#
# Exclusive common numbers.
#
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# Constraints: use only while loop and random module to generate numbers

import random

random_list_1, random_list_2, random_list_3 = ([],[],[])


while len(random_list_2) <= 9 or len(random_list_2) <= 9:
    random_list_1.append(
        random.randint(1,11)
    )
    random_list_2.append(
        random.randint(1,11)
    )


random_list_3 = list(set(random_list_1 + random_list_2))
print('\tTask 2\n')
print(f'First random list: {random_list_1}')
print(f'Second random list: {random_list_2}')
print(f'Lists without any duplicates: {random_list_3}\n')

# Task 3
#
# Extracting numbers.
#
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration

list_100 = []
counter = 1
separate_list=[]


while len(list_100) <=99:
    list_100.append(counter)

    if list_100[-1] % 7 == 0 and list_100[-1] % 5 != 0:
        separate_list.append(counter)

    counter += 1

print('\tTask 3\n')
print(f'List of numbers from 1 to 100: {list_100}')
print(f'Numbers divisible by 7 but not by 5: {separate_list}')