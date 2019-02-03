#!/usr/bin/env python3

'''
----------------------------------------------------
Assignment: dict_lab.py
Author: visokoo | Created: 2/1/2019
ChangeLog: 2/2/2019, Created file

Learn the basic ins and outs of Python dictionaries and sets
----------------------------------------------------
'''

# Dictionaries 1
dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(dict1)
dict1.pop("cake")
print(dict1)
dict1.update({"fruit": "Mango"})
print(dict1.keys())
print(dict1.values())
print("cake" in dict1.keys())
print("Mango" in dict1.values())

# Dictionaries 2
dict2 = {}
for key, value in dict1.items():
    occurrences = value.count("t")
    dict2.update({key: occurrences})
print(dict2)

# Sets 1
s2 = set(i for i in list(range(20)) if i % 2 == 0)
s3 = set(i for i in list(range(20)) if i % 3 == 0)
s4 = set(i for i in list(range(20)) if i % 4 == 0)
combined_sets = (s2, s3, s4)
for sets in combined_sets:
  print(sets)

print(s3 < s2)
print(s4 < s2)

# Sets 2
s1 = {'p', 'y', 't', 'h', 'o', 'n'}
s1.update("i")
print(s1)
fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
print(fs)

print(s1.union(fs))
print(s1.intersection(fs))
