# coding=utf-8
u"""
Missing integer.

Write a function:

int solution(int A[], int N);

that, given a non-empty zero-indexed array A of N integers,
returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range
[−2,147,483,648..2,147,483,647].

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N),
beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""


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
