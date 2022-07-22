"""
Divisors  
Exercise 4 (and Solution)
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
 (If you don’t know what a divisor is, 
it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

print('Enter a number: ')
num = int(input())

def find_divisors(n):
    divs = []
    for i in range(1,n+1):
        if n % i == 0:
            divs.append(i)
        else:
            continue

    return divs 

print('The divisors of ', num, 'are : ')
print(find_divisors(num))

