# Task 1
#
# A simple function.
#
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print "My favorite movie is named {name}".

print(
    '\n\t**** Task_1 ****\n'
)
print(
    'A simple function.\n'
)

movie_name = input( # receiving information from user regarding his favorite movie
    'Please write your favorite movie: '
)


def print_favorit_movie(movie_name): # creating function for display final result
    print(
        f'My favorite movie is named {movie_name.title()}'
    )
if movie_name == "": #checking user input, is it empty or not.
    print("Unfortunately you didn't write any movie") # in case empty input
else:
    print_favorit_movie(movie_name) # is case correct input


# Task 2
#
# Creating a dictionary.
#
# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
# Make the function print out the values of the dictionary to make sure that it works as intended.

print(
    '\n\t**** Task_2 ****\n'
)
print(
    'Creating a dictionary\n'
)
# Request from user country and capital
(country_name, country_capital) = (input(
    'Please write a country name: '
),
                                   input(
    'Please write a capital of this country: '
))

def make_country(name, capital):
    if name == "" or capital == "": # if name or capital is empty we will print error message to user
        print(
            "You didn't write a country name or capital..."
        )
        return None  # Return None if input incorrect
    else:
        country_dict = {
            'name': name, 'capital': capital
        }
        print(country_dict)
        print(
            f'Country name: {name}, and capital is: {capital}'
        )
        return country_dict  # Returning dictionary

# call function
country = make_country(country_name, country_capital)


# Task 3
#
# A simple calculator.
#
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter >
# > (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) >
# > as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
#
# the call make_operation('+', 7, 7, 2) should return 16
# the call make_operation('-', 5, 5, -10, -20) should return 30
# the call make_operation('*', 7, 6) should return 42

print(
    '\n\t**** Task_3 ****\n'
)
print(
    'A simple calculator\n'
)

def make_operation(operator, *args):
    try:
        # Convert all arguments to numbers
        args = [float(arg) for arg in args]
    except ValueError:
        return print(
            'Error: One or more arguments are not numbers.'
        )

    # Check if the operator is valid
    if operator not in ["+", "-", "*"]:
        return print(
            'Error: Unsupported operator! Use +, -, or *.'
        )

    # Start calculation
    result = args[0]  # First number
    for i in args[1:]:  # Go through the rest of the numbers
        if operator == "+":
            result += i
        elif operator == "-":
            result -= i
        elif operator == "*":
            result *= i
    return print(f'Result: {int(result)}')

# Examples of using the function
make_operation('+', 7, 7, 2)  # Use + operator
make_operation("+", 1, 2, 3, 'b')  # Argument "b" is not a number
make_operation('-', 5, 5, -10, -20)  # Use - operator
make_operation('*', 7, 6)  # Use * operator
make_operation("/", 1, 2, 3, 4, 5, 6)  # Wrong operator

# Input from the user
operator = input(
    'Enter operator (+, -, *): '
).strip()
arguments = input(
    'Enter numbers separated by commas (e.g., 1,2,3): '
)

# Process user input
args = arguments.split(",")  # Split input into parts
args = [arg.strip() for arg in args]  # Remove spaces

# Call the function
make_operation(operator, *args)