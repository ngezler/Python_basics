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

r1 = Robot("Tom", "Red", 30) 
r2 = Robot("Tim", "blue", 40)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def  sit_down(self):
        self.is_sitting = True
    
    def  stand_up(self):
        self.is_sitting = False
    
p1 = Person("Alice", "aggressive", False)
p2 = Person("Bowa", " talkactive", True)

#1st person owns robot 2
p1.robot_owned = r2
p2.robot_owned = r1


p1.robot_owned.introduce_self()