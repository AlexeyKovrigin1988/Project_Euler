""" The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? """

import math


def issimple(a):
    r = math.ceil(math.sqrt(a))
    lst = []
    for i in range(3, r):
        if a % i == 0:
            if issimple(i) == []:
                lst.append(i)
    return lst


r = issimple(600851475143)
print(max(r))
