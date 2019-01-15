#improting the modules in python    
import random
import sys
import os

print('hello World')
# single line comments
''' 
multi line comments
'''


#below is a variable
name = "mongezi"
print(name)


''' 
        five main data types in python
numbers, Strings, Lists, Tuples and Dictionaries
'''

'''
    ________seven tyepes_____________
    + plus
    - minus
    * multiplication
    / division->gives a float value
    % modulus->shows you the remainder after a perfoming a division
    ** power
    // division->gives a whole number (int)
 '''

 print("10 + 10 =", 10 + 10)
 print("10 - 5  =", 10 - 5)
 print("5 * 5   =", 5 * 5)
 print("5 ** 2  =", 5 ** 2)
 print("10 % 3  =", 10 % 3)
 print("10 // 2 =", 10 // 2)
#place a comma after the string before starting calculations

 # order of operation in python
 print(10 - 2 / 5 * 3 ** 2)
 print((10 -2)/5 * 3 ** 2)

 quote = "\"Always remember your password to be able to login"
 
 multi_line_quote = ''' they all 
    work the same way 
    '''
#below we are joining two strings
new_str = quote +  multi_line_quote

#formart using print
print("%s %s %s" %('I like the qoute', quote, multi_line_quote))

#removing the newline when printing 
print("I do not like unecessary new lines every time", end="")

#printing something a multiple different time
print("\n" * 5)

''' ______________________________________________________________________
                    Lists_in
    ->a list will allow you to create a list of values then munipulate them
    -> they are indexed from 0
    ->
'''

grocery_list = ['iwisa', 'spinach', 'samp', 'carrot']
#retriving values by their indexes
print('the second item in the list is', grocery_list[1])

#retriving values in a certain range
print(grocery_list[1:3])

#you can create lists within lists

other_events = ['write code', 'test code', 'fix bugs', 'deploy']

to_do_list = [other_events, grocery_list]

#print the whole list
print(to_do_list)

#print by indexes this should print spinach
print(to_do_list[1][1])

#lets just play with built in methods that we are more likely to use on lists

grocery_list.append('spinach')

grocery_list.insert(1,"pumkin")

grocery_list.remove("samp")

grocery_list.sort()

grocery_list.reverse()

print(to_do_list)


# we can combine lists too just as we can combine the strings

to_do_list = grocery_list + other_events
print(to_do_list)

print('the lenght of the list is ', len(to_do_list))

print('the maximum item in the list ', max(to_do_list))

print('the minimum item in the list ', max(to_do_list))


'''
    _____________________________________________________________________________________
                    tuples
->they are similar to lists
->the main difference is unlike like you can't change a tuple after it is created
->you can use tuples for values that you do not want to be changed
'''

my_PI_tuple =  (2,4,5,76,7,)

#convert a tuple to list to be able to make changes
new_tuple = list(my_PI_tuple)

#convert a list to tuple are perfoming the changes
new_list = tuple(new_tuple)

#all other methods works as the lists

'''
    _________________________________________________________________________________________
                Dictionaries and maps
    ->Dictionaries are made of values with unique keys for each value stored
    ->they are simillar to lists but they can't be joined
    ->use the curle braces
'''

super_villians = {'Fiddler' : 'Isaac Bowin',
                    'captain cold ' : 'Leonard Snart',
                    'weather changer' : 'Mark Mardon',
                    'Mirror Master' : 'Sam Scudder'
                    'pied piper' : 'Thomas Scudder'}

#print whole dictionary
print(super_villians)

#print with keys
print(super_villians['captain cold'])

print(super_villians['Fiddler'])

#changing the values in the keys
super_villians['piep piper'] = 'Hartley Rathaway'

#print the lenght of a dictionary
print(len(super_villians))

#get a specific value in the dictionaty
print(super_villians.get('pied piper'))

#getting the list of keys
print(super_villians.keys())

#get the vlist of dictionary values
print(super_villians.values())

'''
         ______________________________________________________________________________________________________
                            conditionals
         -> if ---------- exec when the statement is true
         -> else ------------exec when the first condition is not meet
         -> elif -------------when working with multiple statements
         -> logical operators below are used to combine conditions
         -> and or not
'''

age = 16

if (age > 6 and age < 13) :
    print('you are at primary school')
elif (age > 12 and age < 18) :
    print('you are at high school')
elif (age > 17 and age < 25) :
    print('you are a tetiary student')
else :
    print("you are in the working category")

'''
        __________________________________________________________________________________________________
                        looping
        ->this will perform an action a certain numbe of times
'''
for x in range(0,10):
    print(x, ' ', end="")

#you can iterate through a list using a forloop
fruit_list = ['apple', 'banana', 'orange', 'grape']

for i in fruit_list:
    print(y)

#defined values in a list
for i 