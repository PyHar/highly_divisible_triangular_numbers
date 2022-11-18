import math

def triangular_numbers (n):
    a = 1
    b = 1

    for i in range (1, n + 1):
            f=open ('output.txt', 'wt' )
            print(b, end = ' ', file = f)
            print(b, end = ' ')
            a = a + 1
            b = a + a

n = 8
triangular_numbers(n)

