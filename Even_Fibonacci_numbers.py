spisok0 = []
spisok1 = []
x = 1

while x <= 4000000:
    x = x * 1.6180339887383030068527324379639
    x = round(x)
    if x % 2.0 == 0:
        spisok0.append(x)
    else:
        spisok1.append(x)

else:
    print(spisok0)
    print(spisok1)

print("Symma =", sum(spisok0))
print("Symma1 =", sum(spisok1))
print('Hello')
