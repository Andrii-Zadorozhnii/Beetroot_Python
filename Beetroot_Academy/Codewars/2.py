# Create a method to see whether the string is ALL CAPS.
#
# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
# In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

def is_uppercase(s):
    return s.isupper() or not any(c.isalpha() for c in s)

# Sometimes, I want to quickly be able to convert miles per imperial gallon (mpg) into kilometers per liter (kpl).
#
# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).
#
# Make sure to round off the result to two decimal points.
#
# Some useful associations relevant to this kata:
#
# 1 Imperial Gallon = 4.54609188 litres
# 1 Mile = 1.609344 kilometres
