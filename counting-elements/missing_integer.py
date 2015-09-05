# coding=utf-8
"""https://codility.com/demo/take-sample-test/missing_integer/."""


def solution(A):
    """Solution."""
    N = len(A)
    numbers = set([x for x in range(1, N + 1)])
    set_A = set([x for x in A if x > 0])
    for n in set_A:
        numbers.discard(n)
    if len(numbers):
        return min(numbers)
    else:
        return N + 1
