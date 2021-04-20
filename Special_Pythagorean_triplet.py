""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

num = 1000

for c in range(1, num):
    for b in range(1, c):
        for a in range(1, b):
            if b ** 2 == c ** 2 - a ** 2 and a + b + c == 1000:
                print(a * b * c)