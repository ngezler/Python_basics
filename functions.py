import random
import sys
import os

#working with functions in python

def AddNumber(num1, num2):
    sum = num1 + num2
    return sum

#function call
print("the sum is = " + str(AddNumber(1, 5)))

#using sys for getting info from the user
print("What is your name")

name = sys.stdin.readline()

print("hello ", name)