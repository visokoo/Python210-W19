'''
----------------------------------------------------
Assignment: fizz_buzz.py
Author: visokoo | Created: 1/20/2019
ChangeLog: 1/20/2019, Created file

Write a program that prints the numbers from 1 - 100 inclusive.
For multiples of three, print "Fizz", multiples of five, print "Buzz."
Numbers that are multiples of both, print "FizzBuzz."
'''

def fizz_buzz(n):
  for num in range(n):
    if num % 5 == 0 and num % 10 == 0:
      msg = "FizzBuzz"
    elif num % 5 == 0:
      msg = "Fizz"
    elif num % 10 == 0:
      msg = "Buzz"
    else:
      msg = num
    print(msg)

fizz_buzz(101)