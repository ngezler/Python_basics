import random
import sys
import os

long_str = "I'm walking to town today"

#print the first four characters
print("first three characters")
print(long_str[0:3])

#printing the last five characters
print("lats five character")
print(long_str[-5:])

#print everything up to the last 5 characters
print("going up to the last five characters")
print(long_str[:-5])

#joining two string together
print(long_str[:-5] + "tomorrow")
print(long_str[:4] + "mongezi")

#handling formatting
print("%c is a %s letter in my name and %d number is my favourite %.5f"%
('x', 'faborite', 7, 0.12))

#capitalise the first letter of a string
my_str = "i am going home"

print(my_str.capitalize())

#finding the index value of a string
print(my_str.find("home"))
#return true or false on valuesn state
print(my_str.isalpha())

#
print(my_str.isalnum())

#
print(len(my_str))
#
# print(long_string.replace("home","house"))

#strip white spaces
print(my_str.strip())

quote_list = my_str.split(" ")

print(quote_list)