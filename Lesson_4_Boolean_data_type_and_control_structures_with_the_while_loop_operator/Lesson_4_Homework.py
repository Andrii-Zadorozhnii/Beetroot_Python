#Task 1

#String manipulation
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
# If the string length is less than 2, return instead of the empty string.
#Sample String: 'helloworld'
#Expected Result : 'held'
#Sample String: 'my'
#Expected Result : 'mymy'
#Sample String: 'x'
#Expected Result: Empty String
#Tips:
#Use built-in function len() on an input string
#Use positive indexing to get the first characters of a string and negative indexing to get the last characters

def string_check(word):
    if len(word) < 2:
        return ""
    else:
        return word[:2] + word[-2:]

# Test cases
print(string_check('helloworld'))
print(string_check('my'))
print(string_check('x'))


#Task 2

#The valid phone number program.
#Make a program that checks if a string is in the right format for a phone number. 
# The program should check that the string contains only numerical characters and is only 10 characters long. 
# Print a suitable message depending on the outcome of the string evaluation.

def valid_phone_number(phone):
    if len(phone) == 10 and phone.isdigit():
        print("Valid phone number")
    else:
        print("Invalid phone number")

# Test cases
valid_phone_number("1234567890")
valid_phone_number("12345abc90")
valid_phone_number("1234")

#Task 3

#The math quiz program.
#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.

correct_answer = 5 * 3
user_answer = int(input("What is 5 * 3? "))

if user_answer == correct_answer:
    print("Correct!")
else:
    print("Wrong!")


#Task 4

#The name check.
#Write a program that has a variable with your name stored ( in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
# if your input is “Anton” and the stored name is “anton”, it should return True.

stored_name = "anton"
user_input = input("Enter your name: ").lower()
if user_input == stored_name:
    print(True)
else:
    print(False)
