'''
----------------------------------------------------
Assignment: Python Push Ups - Warmup Part 2 - string_bits.py
Author: visokoo | Created: 1/16/2019
ChangeLog: 1/16/2019, Created file

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

----------------------------------------------------

'''

def string_bits(str):
  new_str = ""
  for position in range(0, len(str), 2):
    new_str += str[position]
  return new_str
