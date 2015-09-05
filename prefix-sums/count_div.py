# coding=utf-8
u"""https://codility.com/demo/take-sample-test/count_div/."""
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
