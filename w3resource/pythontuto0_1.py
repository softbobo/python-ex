#!/usr/bin/python3
#written by softbobo 180807

for n in range(2,11):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')