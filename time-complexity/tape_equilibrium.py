"""https://codility.com/demo/take-sample-test/tape_equilibrium/."""


from math import fabs
from sys import maxsize


def solution(A):
    """Solution."""
    a_sum = sum(A)
    part_a = A[:1][0]
    part_b = a_sum - part_a
    min_diff = maxsize
    for i in range(1, len(A)):
        diff = fabs(part_a - part_b)
        part_a += A[i]
        part_b -= A[i]
        if diff < min_diff:
            min_diff = diff
    return int(min_diff)


if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))
