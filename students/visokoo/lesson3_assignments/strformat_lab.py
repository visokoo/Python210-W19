'''
----------------------------------------------------
Assignment: strformat_lab.py
Author: visokoo | Created: 1/24/2019
ChangeLog: 1/24/2019, Created file

Task One: Write a format string that will take this tuple:
( 2, 123.4567, 10000, 12345.67) and produce:
'file_002 :   123.46, 1.00e+04, 1.23e+04'

Task Two: Use results from task one and try diff ways to format

Task Three: Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
to take an arbitrary number of values

Task Four: Given a 5 element tuple: ( 4, 30, 2017, 2, 27), use string
formatting to print: '02 27 2017 04 30'

Task Five: Given this list: ['oranges', 1.3, 'lemons', 1.1], write a fstring
that will display: "The weight of an orange is 1.3 and the weight of a lemon is 1.1"

Task Six: Write some Python code to print a table of several rows, each with a name,
an age and a cost. Make sure some of the costs are in the hundreds and thousands to
test your alignment specifiers.
----------------------------------------------------
'''

def str_format_t1(object):
  '''
    Good old string formatting specifying each item in the given object
  '''
  formatted_string = "file_00{:d} :  {:.2f}, {:.2e}, {:3.2e}".format(object[0], object[1], object[2], object[3])
  return formatted_string

def str_format_t2_kwargs(object):
  '''
    String formatting w/ kwargs
  '''
  formatted_string = "file_00{:d} :  {:.2f}, {:.2e}, {:3.2e}".format(*object)
  return formatted_string

def str_format_t2_fstring(object):
  '''
    String formatting with fstrings. Looks like it doesn't support unpacking like
    .format does so you'll have to specify each item in the tuple.
  '''
  formatted_string = f"file_00{object[0]} :  {object[1]:.2f}, {object[2]:.2e}, {object[3]:3.2e}"
  return formatted_string

def arbitrary(object):
  '''
    Making it so it doesn't matter how many args are provided it'll still work
  '''
  tuple_length = len(object)
  formatted_string = ("the {} numbers are: " + ", ".join(["{}"] * tuple_length)).format(tuple_length, *object)
  return formatted_string

def padding(object):
  '''
    Always return 2 digits if it isn't already and rearrange via index
  '''
  formatted_string = "{:02d} {:02d} {:02d} {:02d} {:02d}".format(object[3], object[4], object[2], object[0], object[1])
  return formatted_string

def fstring(object):
  '''
    Using fstring and some slicing to get rid of the extra 's' in both fruits
  '''
  fruit1, weight1, fruit2, weight2 = object
  return f"The weight of an {fruit1[0:len(fruit1)-1]} is {weight1} and the weight of a {fruit2[0:len(fruit2)-1]} is {weight2}"

def fstring_modified(object):
  '''
    Using fstring to do some simple string functions and math
  '''
  fruit1, weight1, fruit2, weight2 = object
  return f"The weight of an {fruit1[0:len(fruit1)-1].upper()} is {weight1} and the weight of a {fruit2[0:len(fruit2)-1].upper()} is {weight2}"

def alignments(object):
  '''
    Printing out a nice table using alignment specifiers
  '''
  print("{:20}{:20}{:20}".format("Name", "Age", "Cost"))
  for listing in object:
    print("{:20}{:20}{:20}".format(*listing))

tuple = ( 2, 123.4567, 10000, 12345.67)
simple_tuple = (12, 31, 88, 6, 22, 89)
five_element_tuple = (4, 30, 2017, 2, 27)
fruit_list = ['oranges', 1.3, 'lemons', 1.1]
dogs = (('Sparky', '2', '$17000'), ('Popcorn', '1', '$2500'), ('Peanut', '3', '$1000'))
# print(str_format_t1(tuple))
# print(str_format_t2_kwargs(tuple))
# print(str_format_t2_fstring(tuple))
# print(arbitrary(simple_tuple))
# print(padding(five_element_tuple))
# print(fstring(fruit_list))
# print(fstring_modified(fruit_list))
# alignments(dogs)