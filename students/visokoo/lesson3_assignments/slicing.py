'''
----------------------------------------------------
Assignment: slicing.py
Author: visokoo | Created: 1/23/2019
ChangeLog: 1/23/2019, Created file

Write some functions that take a sequence as an argument, and return a copy of that sequence:

- with the first and last items exchanged.
- with every other item removed.
- with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
- with the elements reversed (just with slicing).
- with the last third, then first third, then the middle third in the new order.
----------------------------------------------------
'''

def flipped(seq):
  '''
    first = first item of the parameter seq
    last = last item of the parameter seq
    middle = the rest of the items besides above 2

    return a string with last_char and first_char flipped
  '''
  first = seq[0:1]
  last = seq[-1:]
  middle = seq[1:-1]
  return last + middle + first

def every_other(seq):
  '''
    utilizing stepping in slicing of sequences to avoid every other
  '''
  return seq[0:len(seq):2]

def first_last_four_removed(seq):
  '''
    remove the first and last four items and iterate every other
  '''
  return seq[4:-4:2]

def reversed(seq):
  '''
   reverse the items in sequence
  '''
  return seq[::-1]

def thirds(seq):
  '''
    with the last third, then first third, then the middle third in the new order
  '''
  last_third = seq[-3:]
  first_third = seq[0:3]
  middle_third = seq[3:-3]
  return last_third + first_third + middle_third

# Tests
str = "supercalifragilistic"
tuple = ('blah', 1, 'blah2', 'blah3', 'blah4', 2, 54, 13, 12, 5, 32, 31, 42, 3)

assert flipped(str) == "cupercalifragilistis"
assert flipped(tuple) == (3, 1, 'blah2', 'blah3', 'blah4', 2, 54, 13, 12, 5, 32, 31, 42, 'blah')
assert every_other(str) == "sprairglsi"
assert every_other(tuple) == ('blah', 'blah2', 'blah4', 54, 12, 32, 42)
assert first_last_four_removed(str) == "rairgl"
assert first_last_four_removed(tuple) == ('blah4', 54, 12)
assert reversed(str) == "citsiligarfilacrepus"
assert reversed(tuple) == (3, 42, 31, 32, 5, 12, 13, 54, 2, 'blah4', 'blah3', 'blah2', 1, 'blah')
assert thirds(str) == "ticsupercalifragilis"
assert thirds(tuple) == (31, 42, 3, 'blah', 1, 'blah2', 'blah3', 'blah4', 2, 54, 13, 12, 5, 32)

print("All Tests passed!")