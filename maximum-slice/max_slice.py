"""
https://codility.com/programmers/task/max_slice_sum
"""
import unittest


class TestMaxDoubleSliceSum(unittest.TestCase):

    def tests(self):
        """Tests."""
        self.assertEqual(solution([3, 2, -6, 4, 0]), 5)
        self.assertEqual(solution([-11]), -11)
        self.assertEqual(solution([-11, 1]), 1)
        self.assertEqual(solution([-11, -23, -35]), -11)


def solution(A):
    n = len(A)
    if n == 1:
        return A[0]
    maxx = max(A)
    if maxx < 0:
        return maxx
    max_sum_slice = 0
    max_sum_total = 0
    for i in range(n):
        max_sum_slice = max(0, max_sum_slice + A[i])
        max_sum_total = max(max_sum_total, max_sum_slice)

    return max_sum_total


if __name__ == '__main__':
    unittest.main()
