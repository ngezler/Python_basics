import random
import sys
import os

#we are reading and writting to the file
test_file = open("test.txt", "w+")
print(test_file.mode)

print(test_file.name)
for i in range(5):
        test_file.write("I am a line %d\n"%(i+1))

test_file.close()

test_file = open("test.txt", "r+")
text_file = test_file.read()
print(text_file)

os.remove("test.txt")