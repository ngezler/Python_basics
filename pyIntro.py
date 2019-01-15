#importing the modules
import random
import sys
import os 

#variable a place to store a value
greetings = "hello World"

print(greetings )

#Lists
print('test2')
Grocery_list = ['juice', 'potatoes', 'rice', 'beans']

print('first Item :', Grocery_list[0])

#test3 change the value of an item in the list
Grocery_list[0] = "100% juice"
print("new item on the list: ", Grocery_list[0])

#list subsets
print(Grocery_list[0:2])

other_events = ['Python', 'Excel', 'Power BI']

#list of lists list can be stored as list
print("below are lists found within lists :")
to_do_list = [Grocery_list, other_events]
print(to_do_list)

#getting the secod item out of the list (2D array)
print("treat this as a two dimensional array infact it is a 2d:")
print(to_do_list[0][1] + " is in box1 position2")

#append items simple places the item at the end of the list
other_events.append('Excel')
print(" ")
print(other_events)

#manipulating the list items and sorting 
other_events.insert(1, "C#")

other_events.remove('Excel')

other_events.sort()

other_events.reverse()

del other_events[1]

print(to_do_list)

#combining list and get the lenght of the list by using len function

print("combining the lists")
to_do_list2 = other_events + Grocery_list
print(to_do_list)
print(len(to_do_list2))

print(min(to_do_list2))
print(max(to_do_list2))

#tuples can't change a list after it is created
pi_tuple = (2,1,4,2,6,7,8)

#when you want to make changes in a turple convert it to a list type cast to list
new_list = list(pi_tuple)
#turning it back from a list to a tuple
new_tuple = tuple(new_list)
print("                  this is tuple business")
print(new_tuple)

#dictionaries and maps contain values and keys casn't be joined

majita_kasi = {'mtshepana' : 'Le bhojwa',
                'magesh' : 'Le pantsula',
                'spitjo' : 'm repa'}

print("ke " + majita_kasi['mtshepana'])

del majita_kasi['spitjo']

majita_kasi['mtshepana'] = "m repa"

print(len(majita_kasi))

print(majita_kasi.get("mtshepana"))

print(majita_kasi.keys())

print(majita_kasi.values())

