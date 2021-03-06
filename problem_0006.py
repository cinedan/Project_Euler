"""
Project Euler Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import sys 

# 'naive' solution runs in linear time and linear space with respect to n
def naive(n):
    sum_n = sum(range(1,n+1))
    return sum([i * i for i in range(1,n+1)]) - (sum_n * sum_n)

# 'efficient' uses formulas to find the solution in constant time and space
def efficient(n):
    sum_n = n * (n + 1) // 2
    sum_n_squared = n * (n + 1) * (2 * n + 1) // 6
    return sum_n_squared - (sum_n * sum_n)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        print("Up to what value do you want to calculate? ")
        n = int(input())
    print(n)
    naive_sol = naive(n)
    eff_sol = efficient(n)
    print("result = ", naive_sol, eff_sol)
