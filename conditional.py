import random
import sys
import os

#working qith if else elif statements

speed = input("enter your current speed : ")
lim = int(speed)   
   
if lim > 120:
       print("you have exceeded the speed limit on this road")
elif lim < 40:
           print("your speed is too low ")
else:
    print("you are driving at a normal speed")

#combining conditions with logical operators and not  or
age = int(input("enter your current age |-> "))

if ((age>=1) and (age <= 21)):
    print("you can get a birth day")
elif ((age < 30) or (age == 31)):
    print("you a not get a thing")
elif ((age == 30) or (age == 70)):
    print("will giv e you the birth day")
elif not(age >= 80):
    print("you are young")
else:
    print("we don't know what to do will see when your birth day comes")
    