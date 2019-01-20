'''
----------------------------------------------------
Assignment: series.py
Author: visokoo | Created: 1/17/2019
ChangeLog: 1/17/2019, Created file

Write 3 functions: fibonacci, lucas, and sum_series and some tests
for the functionality.

Fibonacci:
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...

Lucas:
The Lucas Numbers are a related series of integers that start with the values
2 and 1 rather than 0 and 1. The resulting series looks like this:
2, 1, 3, 4, 7, 11, 18, 29, ...

sum_series:
Create a function with one required parameter and two optional parameters. The required
parameter will determine which element in the series to print. The two optional parameters
will have default values of 0 and 1 and will determine the first two values for the series
to be produced.
'''

def fibonacci(n):
  '''
    fib(n) = fib(n-2) + fib(n-1)
    Given the value n, call the sum_series function with that value
    and return the fibonacci sequence at the nth index
  '''
  return sum_series(n)

def lucas(n):
  '''
    Formula is the same as fib, but starting values are 2 and 1 respectively
    Given the value n, call the sum_series function with that value and
    return the lucas sequence at the nth index
  '''
  return sum_series(n, v1=2, v2=0)

def sum_series(n, v1=0, v2=1):
  '''
    compute the nth value of a summation series.

    :param v1=0: value of zeroth element in the series
    :param v2=1: value of first element in the series

    This function should generalize the fibonacci() and the lucas(),
    so that this function works for any first two numbers for a sum series.
    Once generalized that way, sum_series(n, 0, 1) should be equivalent to
    fibonacci(n). And sum_series(n, 2, 1) should be equivalent to lucas(n).
  '''
  if v1 is 2:
    if n == 0:
      return 2
    elif n == 1:
      return 1
    else:
      return sum_series(n - 2, v1=v1, v2=v2) + sum_series(n - 1, v1=v1, v2=v2)
  else:
    if n > 1:
      return sum_series(n - 2) + sum_series(n - 1)
    return n

if __name__ == "__main__":
  # run some tests to make sure the fibonacci() is returning expected values.
  assert fibonacci(0) == 0
  assert fibonacci(1) == 1
  assert fibonacci(2) == 1
  assert fibonacci(3) == 2
  assert fibonacci(4) == 3
  assert fibonacci(5) == 5
  assert fibonacci(6) == 8
  assert fibonacci(7) == 13
  # run some tests to make sure the lucas() is returning expected values.
  assert lucas(0) == 2
  assert lucas(1) == 1
  assert lucas(4) == 7
  # make sure sum_series outputs match fibonacci() and lucas() outputs.
  assert sum_series(5) == fibonacci(5)
  assert sum_series(5, 2, 1) == lucas(5)

  print("Tests passed.")