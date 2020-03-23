"""
Project Euler Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys
import math

def naive(n):
  tot = 0
  for i in range(1,n):
    tot += i if i%3==0 or i%5==0 else 0
  return tot

def __arithmeticSum(n):
  return int((n * n - n) / 2)

def constant(n):
  threes = 3 * __arithmeticSum(math.ceil(n / 3))
  fives = 5 * __arithmeticSum(math.ceil(n / 5))
  fifteens = 15 * __arithmeticSum(math.ceil(n / 15))

  return threes + fives - fifteens

if __name__ == '__main__':
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
  else:
    n = 1000

  print(naive(n))
  print(constant(n))
