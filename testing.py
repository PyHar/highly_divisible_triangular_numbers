#first we import what we need
from math import *
import sys

#stdout so we can print result into the file
original_stdout = sys.stdout
#define our variable
def triangular_numbers (n):
    a = 1
    b = 1
#for loop
    for i in range (1, n + 1):
        #print to console
        print (b, end = ' ')
        with open('output.txt', 'a') as f:
            sys.stdout = f
            #print to output.txt file
            print (b, end = ' ')
            sys.stdout = original_stdout


        a = a + 1
        b = a + a
#here we can define how many numbers we want to print out
n = 10
triangular_numbers(n)


