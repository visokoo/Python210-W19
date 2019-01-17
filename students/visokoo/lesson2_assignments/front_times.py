'''
----------------------------------------------------
Assignment: Python Push Ups - Warmup Part 2 - front_times.py
Author: visokoo | Created: 1/16/2019
ChangeLog: 1/16/2019, Created file

Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
----------------------------------------------------

'''

def front_times(str, n):
  front = str[:3]
  return front * n
