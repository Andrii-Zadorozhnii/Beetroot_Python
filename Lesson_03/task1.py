from dateutil.rrule import weekday

print(
    """
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

"Good day <name>! <day> is a perfect day to learn some python."

Note that  <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.
    """
)
print('__________HOMEWORK_________\n')
name = "Andrii"
day = "saturday"

print(
    f'Good day {name.capitalize()}! {day.capitalize()} is a perfect day to learn some python'
)

message = 'Good day {}! {} is a perfect day to learn some python'
print(
    message.format(name.capitalize(), day.capitalize())
)

print(
    'Good day {0}! {1} is a perfect day to learn some python'.format(name, day)
)

print(
    'Good day %s! %s is a perfect day to learn some python' % (name, day)
)
