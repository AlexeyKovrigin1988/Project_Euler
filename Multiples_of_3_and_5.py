spisokX = []
spisokY = []

x = 0
while x <= 999:
    if x % 5.0 > 0:
        spisokX.append(x)
        x = x + 3

    else:
        print(x)
        x = x + 3


else:
    # x = x - 3
    print("Symma x = ", x)

y = 0
while y <= 994:
    y = y + 5
    spisokY.append(y)
else:
    # y = y - 5
    print("Symma y= ", y)

print(spisokX)
print(spisokY)

sum(spisokX)
sum(spisokY)
print("Сумма х =", sum(spisokX))
print("Сумма y =", sum(spisokY))
a = sum(spisokX)
b = sum(spisokY)
c = a + b
print("Сумма х и у =", c)

