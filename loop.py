import random
import sys
import os

#loops
x = 0
print("First Test")
while x != 10:
    print(x)
    x = x + 1

print("Second Test")
#you can do the above thing in two lines of code
for x in range(0, 10):
    print(x)

#cycle through list using for loops

languages = ['isXhosa', 'isiZulu', 'Sesotho', 'Setswana']
print("A List Some SA languages\n")
for z in languages:
    print(z)

#define a list to iterate through
print("This is a Defined list  :")

for j in [1,4,56,6,7,7,5,]:
    print(x)
#double up the for 
num_list = [[1,2,3],[10,20,30],[100,200,300]]
print("printing a list within a list")
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


#while loop when you do not know how many times you are going to loop you can use while
random_num = random.randrange(0,1)

while (random_num != 0):
    print(random_num)
    random_num = random.randrange(0,1)

#traditional way of using the while loop
# i = 0

# while (i <= 16):
#     if (i + 2 == 5):
#         print(i)
#     elif(i == 9):
#         break
#     else:
#         i += 1

