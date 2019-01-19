'''
----------------------------------------------------
Assignment: grid_printer.py
Author: visokoo | Created: 1/16/2019
ChangeLog: 1/16/2019, Created file

Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
----------------------------------------------------
'''

def borders(n):
  return " + " + " - " * n

def pillars(n):
  return " | " + " " * (n * 3)

def grid_printer(n):
  print(borders(n) * 2, "+")
  for i in range(n):
    print(pillars(n) * 2, "|", sep=" ")
  print(borders(n) * 2, "+")
  for i in range(n):
    print(pillars(n) * 2, "|", sep=" ")
  print(borders(n) * 2, "+")

def fancy_grid_printer(table_size, grid_size):
  print(borders(grid_size) * table_size, "+")
  for i in range(table_size):
    for j in range(grid_size):
      print(pillars(grid_size) * table_size, "|", sep=" ")
    print(borders(grid_size) * table_size, "+")

while True:
  prompt = input("Standard 2x2 table or fancy table?" + "\n" + "Options: standard/fancy/exit ")
  if prompt.lower() == "standard":
    size = input("Pick a size for your table, larger the number, larger the table. 1 - infinity ")
    grid_printer(int(size))
  elif prompt.lower() == "fancy":
    total_table_size = input("Number of rows and columns? 1 - infinity ")
    width = input("Width of each grid? 1 - infinity ")
    fancy_grid_printer(int(total_table_size), int(width))
  else: break
