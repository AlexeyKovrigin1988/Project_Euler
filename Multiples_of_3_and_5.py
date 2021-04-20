""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

spisokX = []
spisokY = []

x = 0
while x <= 999:
    if x % 5.0 > 0:
        spisokX.append(x)
        x = x + 3

    else:
        x = x + 3

y = 0
while y <= 994:
    y = y + 5
    spisokY.append(y)

print("Сумма х =", sum(spisokX))
print("Сумма y =", sum(spisokY))
a = sum(spisokX)
b = sum(spisokY)
c = a + b
print("Сумма х и у =", c)