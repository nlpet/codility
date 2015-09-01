# coding=utf-8
u"""
Count div.

Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within
the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3,
because there are three numbers divisible by 2 within the range [6..11],
namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
"""
import unittest
from math import floor


def solution(A, B, K):
    """Solution."""
    K = float(K)
    return int(floor(B / K) - floor((A - 1) / K))


class TestCountDiv(unittest.TestCase):

    """Unit tests for counting numbers divisible by K."""

    def tests(self):
        """Tests."""
        self.assertEqual(solution(6, 11, 2), 3)
        self.assertEqual(solution(7, 8, 4), 1)
        self.assertEqual(solution(1, 100, 2), 50)
        self.assertEqual(solution(1, 100, 3), 33)
        self.assertEqual(solution(0, 0, 11), 1)
        self.assertEqual(solution(10, 10, 5), 1)


if __name__ == '__main__':
    unittest.main()
