"""
https://codility.com/programmers/task/ladder
"""
from math import sqrt
import numpy as np

PHI = np.float(1.61803398874989484820458683436563811772030917980576)
SQRT5 = np.float(sqrt(5))


def fib(n):
    n += 1
    phin = np.float(PHI ** n)
    return int((phin - ((-1)**n / phin)) / SQRT5)


def solution(A, B):
    results = []
    for i in range(len(A)):
        results.append(fib(A[i]) % (2**B[i]))
    return results



if __name__ == '__main__':
    A = [4, 4, 5, 5, 1]
    B = [3, 2, 4, 3, 1]
    print(solution(A, B))
