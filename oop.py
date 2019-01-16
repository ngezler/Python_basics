import random
import sys
import os

#oop programing modeling real world problems

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

#constructor to set up or initialise an object
def __init__(self, name, weight, height, sound):
    self.__name = name
    self.__height = height
    self.__weight = weight
    self.__sound = sound



'''self allows the object to refer to its self
   change the object name 
   below we doing seters and getters'''

def set_name(self, __name):
        self.__name = name

def get__name(self):
    return self.__name

def set_weight(self, __weight):
    self.__weight = weight

def get_weight(self):
    return str(self.__sound)

def set_height(self, __height):
    self.__height = height

def get_height(self):
    return str(self.__sound)

def set_sound(self, __sound):
    self.__sound = sound

def get_sound(self):
    return self.__sound

def get_type(self):
    print("Anamal")

def toString(self):
    return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                  self.__height,
                                                                  self.__weight,
                                                                  self.__sound)
                                                                
#creating an object of type animal
def make_Animal(name, weight, height, sound):
        cat = Animal('whiskers', 22, 30, 'miyawu')
        print(cat.toString())

