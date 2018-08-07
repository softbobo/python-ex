#!/usr/bin/python3
#created by softbobo 180807
#link https://www.w3resource.com/python-exercises/python-conditional-exercise-1.php
#successful on 180807

for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        print(n, 'is a multiple of 5 and divisible by 7')

