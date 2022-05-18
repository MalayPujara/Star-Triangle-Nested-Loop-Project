# -*- coding: utf-8 -*-
"""Creating triangular patterns in Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MEC6EUbGP6xRdC0LZ5zWNJUouRv2Ojgb
"""

# To show how to create triangular patterns in python.

# Triangle-1 {Here, we will have two loops; 1st loop for number of rows (x);2nd loop for number of columns}
*
**
***
****
*****
# CODE:-

n=int(input('Enter the Number:'))
for x in range(n):
  for y in range(x+1):
    print("*",end="")
  print()

# Triangle-2 {Here, we will have two loops; 1st loop for number of rows (x);2nd loop for number of columns}
*****
****
***
**
*
# CODE:-

n=int(input('Enter the Number:'))
for x in range(n,0,-1): #(her, the range is (5,0) and -1 is the decrement value);[Decrement value here means the number we are subtracting from x rows w.r.t. number of columns]
  for y in range(x,0,-1):
    print("*",end="")
  print()

# Triangle-3 {Here, we will have two loops; 1st loop for number of rows (x);2nd loop for number of columns}
  *
 ***
*****
# CODE:-

n=int(input('Enter the Number:'))
for x in range(n): #Here,it is n-x-1 to keep space.
  for y in range(n-x-1):
    print(" ",end="") #Here," " is used to keep 1 unit space in 1 row.
  for y in range(2*x+1):
    print("*",end="")
  print()

# Triangle-4 {Here, we will have two loops; 1st loop for number of rows (x);2nd loop for number of columns}
*****
 ***
  *
# CODE:-

n=int(input('Enter the Number:'))
for x in range(n): #Here,it is n-x-1 to keep space.
  for y in range(x):
    print(" ",end="") #Here," " is used to keep 1 unit space in 1 row.
  for y in range(2*(n-x)-1):
    print("*",end="")
  print()
