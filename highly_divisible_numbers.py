#first we import what we need
from math import *
import sys
original_stdout = sys.stdout #stdout so we can print result into the file
def triangleNumbers(n): #define our variable
#for loop
    for i in range (1, n + 1):
        #print to console
        print (i*(i+1)//2,end=' ')
        with open ('output.txt', 'a') as f:
            sys.stdout = f
            #print to output.txt file
            print (i*(i+1)//2,end=' ')
            sys.stdout = original_stdout
n = 10 # how many triangular numbers we want to print
triangleNumbers(n)

def Divisors(n = 0, agg = 0):
    while True:
        n += 1
        agg += n
        #pass function
        yield agg
#define number of divisors
def number_of_divisors(n):
    num_factors = 2
    #square number
    sq = int(n ** 0.5)
    for candidate in range(2, sq):
        if n % candidate == 0:
            num_factors += 2
    if sq * sq == n:
        num_factors -= 1
    return num_factors
#use vectors to find triangle numbers
if __name__ == "__main__":
    current_magnitude = 10
    for num in Divisors():
        #here we can specify how many divisors we want for the number to have
        if number_of_divisors(num) >= 3:
             #print to console
            print("Number is: " + str(num))
            with open('output2.txt', 'a') as f:
                sys.stdout = f
                #print to output2.txt
                print("Number is: " + str(num))
                sys.stdout = original_stdout
            exit(0)
