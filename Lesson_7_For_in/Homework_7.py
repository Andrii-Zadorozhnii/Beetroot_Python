# Task 1
#
# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.

# Receiving some sentence from user
print(
    '\n\t**** Task_1 ****\n'
)
print(
    'Counting unique words\n'
)
input_sentence = input("Please write some sentence: ")

if input_sentence != "":
    print(
        f'You entered sentence: {input_sentence:}\n')
else:
    print(
        "Unfortunately you didn't write anything"
    )


# Separate the words from user and add it to the list
word_list = input_sentence.split()
repeat_dict = {}

# Calculation repeating words and add it to the dictionary
for word in word_list:
    repeat_dict[word.lower()] = repeat_dict.get(word.lower(), 0) + 1

# Showing result to user
for word_name,word_count in repeat_dict.items():
    print(
        f'Word: {word_name.title():15} repeating: {word_count:2} times'
    )

# Task 2
#
# Input data:
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.
#
# The code has to return the dictionary with the sums of the prices by the goods types.
print(
    '\n\t**** Task_2 ****\n'
)
print(
    'Compute the total price of the stock\n'
)
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "ball": 12  #add additional stock item for calculation
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

calculation = dict()
summa = 0

# Checking if stock item is in price, and making calculation in case yes
for stock_item, stock_value in stock.items():
    if stock_item in prices:
        total_price = stock_value * prices[stock_item]
        calculation[stock_item] = total_price
        print(
            f'{stock_item.title():7}: {stock_value:2} items, price per item {prices[stock_item]:3}, total price: {total_price:4} usd'
        )
    else: #in case item don't have a price, we will see current message
        print(
            f'Price for {stock_item} not found =( '
        )
#Final stock calculation
for calculation_value in calculation.values():
    summa += calculation_value
#shoving to user final supermarket budget
print(
    f'\nTotal supermarket budget is: {summa} usd'
)
# Task 3
# List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.
print(
    '\n\t**** Task_3 ****\n'
)
print(
    'List comprehension exercise\n'
)
# Creating list by list generator
list_comprehension = [(x,x**2) for x in range(0, 10)]
# Showing to user generated list
print(
    f'Tuple list: \n{list_comprehension}\n'
)
# Showing to user all calculation in more interesting format
for i in list_comprehension:
    print(
        f'i = {i[0]}, and square = {i[1]}')


# Task 4
#
# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
# Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,

import calendar # import calendar module

print(
    '\n\t**** Task_4 ****\n'
)
print(
    'Weekday list\n'
)

# by generator creating list with a number and weekday
weekday_list = [(i+1, calendar.day_name[i]) for i in range(0,7)]    # Generator {1: "Monday", 2:...
reverse_weekdays_list = [(calendar.day_name[i], i+1) for i in range(0,7)] # Reverse generator {"Monday": 1,

print(
    f'Generated dictionary: {dict(weekday_list)}'
) # Display Generator {1: "Monday", 2:...
print(
    f'Generated reversed dictionary: {dict(reverse_weekdays_list)}'
) # Display reverse generator {"Monday": 1,




