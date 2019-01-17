z'''
----------------------------------------------------
Assignment: Python Push Ups - Warmup Part 1 - near_hundred.py
Author: visokoo | Created: 1/9/2019
ChangeLog: 1/9/2019, Created file 
 Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
 near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
----------------------------------------------------
 '''

 def near_hundred(n):
  return abs(100 - n) <= 10 or abs(200-n) <= 10
