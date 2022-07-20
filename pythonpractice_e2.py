
"""
Odd Or Even 
input if types int equality comparison numbers mod
Exercise 2 (and Solution)
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

 Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

def ask_num(prompt):
    print(prompt)
    n = int(input())

    return n

def check_odd_even(num):
    if num % 2 == 0:
        print('number is even.')
    else:
        print('number is odd.')

def check_four_div(num):
    if num % 4 == 0:
        print('number is divisible by four.')
    else:
        print('number is not divisible by four.')

def check_two_numbers(n1, n2):
    if n1 % n2 == 0:
        print(n1 , ' is divisible by ', n2)
    elif n2 % n1 == 0:
        print(n2, ' is divisible by ', n1)
    else:
        print('numbers are not divisible.')

number = ask_num('Please enter a number to check if it is odd or even. ')
check_odd_even(number)

print('Do you want to continue? Check if divisible by 4. Y/N?')
ans1 = input()
if ans1 == 'Y' or ans1 == 'y':
    check_four_div(number)
else:
    print('You decided not to check divisibility by four.')

ans2 = input('Continue to check 2 random numbers with each other. Y/N?')
if ans2 == 'Y' or ans2 == 'y':
    print('Your two numbers: ')
    num1 = int(input())
    num2 = int(input())
    check_two_numbers(num1, num2)
else:
    print('You decided not to check 2 numbers.')

print('you\'re all done.')
