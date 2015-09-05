# coding=utf-8
u"""Passing cars."""
import unittest


def solution(A):
    """Solution."""
    passing_east = 0
    total_count = 0
    for i in range(len(A)):
        if A[i]:
            total_count += passing_east
        else:
            passing_east += 1
    return total_count if total_count <= 1000000000 else -1


class TestPassingCars(unittest.TestCase):

    """Unit tests for counting numbers divisible by K."""

    def tests(self):
        """Tests."""
        self.assertEqual(solution([0, 1, 1, 1, 0, 1]), 5)
        self.assertEqual(solution([0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(solution([0, 1]), 1)
        self.assertEqual(solution([0]), 0)
        self.assertEqual(solution([1, 1, 1, 1, 0]), 0)
        self.assertEqual(solution([1, 0]), 0)


if __name__ == '__main__':
    unittest.main()
