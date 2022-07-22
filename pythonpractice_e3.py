"""Exercise 3 (and Solution)
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list
 in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller
 than that number given by the user.
"""

test_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def find_less_five(l,n):
    for i in range(len(l)):
        if l[i] < n:
            print(l[i])
        else:
            continue 
    
print('One by One.')
find_less_five(test_list,5)

def find_less_five_list(l, n):
    new = [] 
    count = 0
    for i in range(len(l)):
        if l[i] < n:
            new.append(l[i])
        else:
            continue
       
    return new

print('new list.')
new_list = find_less_five_list(test_list,5)
print(new_list)

print('give me a number, I\'ll check and find numbers smaller than that in list.')
num = int(input())

print(find_less_five_list(test_list, num))