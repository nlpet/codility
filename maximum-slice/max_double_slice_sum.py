"""https://codility.com/programmers/task/max_double_slice_sum"""
import unittest


class TestMaxDoubleSliceSum(unittest.TestCase):

    def tests(self):
        """Tests."""
        self.assertEqual(solution([3, 2, 6, -1, 4, 5, -1, 2]), 17)
        self.assertEqual(solution([1, 1, 0, 10, -100, 10, 0]), 21)


def solution(A):
    ending_at, double_ending_at, result = A[1], 0, 0

    for i in range(2, len(A) - 1):
        double_ending_at = max(double_ending_at + A[i], ending_at)
        result = max(result, double_ending_at)
        ending_at = max(0, max(A[i], ending_at + A[i]))

    return result


if __name__ == '__main__':
    unittest.main()
