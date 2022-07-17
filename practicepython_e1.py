"""
Exercise 1 
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year
that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
from datetime import date 

def ask_name():
    print('Hello. Please enter your name: ')
    name = input()

    return name

def ask_age():
    
    print('Please enter your age in number: ')
    age = int(input())
    
    return age

def year_100(a):

    date_now = date.today()
    current_year = date_now.year 
    birth_year = current_year - a 
    year_100 = birth_year + 100 

    return year_100 

print('Welcome. Press Enter after your answers.')
name_ = ask_name()
age_ = ask_age()

year_they_turn_100 = year_100(age_)

def answer(n, yr):
    print('Dear ', n, ' you will turn 100 years old in ', yr, '.')

answer(name_, year_they_turn_100)

print('I want to repeat it a few more times! How many times should I repeat this? ')
repeats = int(input())

for i in range(repeats):
    answer(name_, year_they_turn_100)



