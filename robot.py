import random
import sys
import os

class Robot:
    #creating a constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name) #self is like this in java

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot() #creates a new robot object
# r2.name = "Tim"
# r2.color = "blue"
# r2.weight = 20
# r1.introduce_self()
# r2.introduce_self()

#creating new robort objects
r1 = Robot("Tom", "Red", 30) 
r2 = Robot("Tim", "blue", 40)

r1.introduce_self()
r2.introduce_self()
