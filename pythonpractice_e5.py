"""Exercise 5 (and Solution)
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
 Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def find_similar(l1, l2):
    len_l1 = len(l1)
    len_l2 = len(l2)

    similar = [] 
    if len_l1 < len_l2 :
        for i in range(len_l1):
            for j in range(len_l2):
                if l1[i] == l2[j]:
                    similar.append(l1[i])
                else:
                    continue
            continue
    else:
        for i in range(len_l2):
            for j in range(len_l1):
                if l2[i] == l1[j] :
                    similar.append(l2[i])
                else:
                    continue
            continue
    if len(similar) == 0:
        print('There are no similar elements.')

    return similar

print('Similar elements in two lists are: ')
print(find_similar(a, b))
    

#randomly generating two lists 
import random 

gen1 = [random.randrange(1,100,1) for i in range(random.randint(3,11))]
gen2 = [random.randrange(1,100,1) for i in range(random.randint(3,11))]

print('list 1 : ', gen1)
print('list 2 : ', gen2)
print('similars: ', find_similar(gen1, gen2))