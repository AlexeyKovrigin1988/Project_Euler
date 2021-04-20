''' By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number? '''

n = 110000
l = [i for i in range(2, n)]
l1 = []
while len(l) > 0:
    l1.append(l[0])
    i = 1
    while i < len(l):
        if l[i] % l[0] == 0:  # A prime number is a number that is divisible by 1 and by itself.
            del l[i]
        else:
            i += 1
    del l[0]

a = l1[10000]
print("Вот оно! =", a)