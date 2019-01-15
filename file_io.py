import random
import sys
import os

#we are reading and writting to the file
test_file = open("test.txt", "wb")
print(test_file.mode)

print(test_file.name)

test_file.write(bytes("write me to the open file\n", 'UTF-8'))

test_file.close()

text_file = test_file.read()
print(text_file)

os.remove("test.txt")