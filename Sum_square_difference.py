""" The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

lst = []
a = int((100*(100+1)*(2*100+1))/6)
print(a)
for i in range(0, 101):
    lst.append(i)
b = sum(lst)*sum(lst)
print(b)
c = b - a
print("Решение: ", c)