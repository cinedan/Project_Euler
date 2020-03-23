"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

# for the given problem definition 'num' will never be more than 6 digits, so this check is technically O(1) complexity
def __palendromeCheck(num):
  strNum = str(num)
  front = 0
  back = len(strNum)-1
  while front < back:
    if strNum[front] != strNum[back]:
      return False
    front += 1
    back -= 1
  return True

# O(n**2 * 6)
def naive(numDigits):
  large = -1
  for a in range(10**(numDigits-1), 10**numDigits):
    for b in range(10**(numDigits-1), 10**numDigits):
      large = max(a*b,large) if __palendromeCheck(a*b) else large
  return large

# should be able to get more efficient by searching backwards from 999*999 along
#  the diagonal of the multiplication table
def upperTriangle(numDigits):
  large = -1
  for a in range((10**numDigits)-1, 10**(numDigits-1) - 1, -1):
    for b in range((10**numDigits)-1, a-1, -1):
      large = max(a*b,large) if __palendromeCheck(a*b) else large
  return large

if __name__ == '__main__':
  if len(sys.argv) == 2:
    numDigits = int(sys.argv[1])
  else:
    numDigits = 3


  print(naive(numDigits))
  print(upperTriangle(numDigits))
