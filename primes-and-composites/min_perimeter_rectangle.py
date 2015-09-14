"""
https://codility.com/programmers/task/min_perimeter_rectangle
"""
from itertools import combinations
from sys import maxint


def find_factors(N, sqrt_N):
    """Find factors of N."""
    if N == 1:
        return [1]
    factors = set()
    for i in range(1, sqrt_N + 1):
        if N % i == 0:
            factors = factors.union({i, N // i})
    return list(factors)


def solution(N):
    """Find min perimeter."""
    min_perimeter = maxint
    sqrt_N = int(round(N ** 0.5))
    factors = find_factors(N, sqrt_N)

    for A, B in list(combinations(factors, 2)) + [(sqrt_N, sqrt_N)]:
        perimeter = 2 * (A + B)
        if A * B == N and perimeter < min_perimeter:
            min_perimeter = perimeter
    return min_perimeter


if __name__ == '__main__':
    N = 101
    print solution(N)
