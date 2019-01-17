'''
----------------------------------------------------
Assignment: Python Push Ups - Warmup Part 1 - pos_neg.py
Author: visokoo | Created: 1/9/2019
ChangeLog: 1/9/2019, Created file 

Given 2 int values, return True if one is negative and one is 
positive. Except if the parameter "negative" is True, then 
return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
----------------------------------------------------
 '''

def pos_neg(a, b, negative):
  if negative == True:
    return (a < 0 and b < 0)
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)

