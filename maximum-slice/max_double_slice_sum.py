"""https://codility.com/programmers/task/max_double_slice_sum"""
import unittest


class TestMaxDoubleSliceSum(unittest.TestCase):

    def tests(self):
        """Tests."""
        self.assertEqual(solution([3, 2, 6, -1, 4, 5, -1, 2]), 17)
        self.assertEqual(solution([1, 1, 0, 10, -100, 10, 0]), 21)


def solution(A):
    length = len(A)
    ending_at = [0] * length
    if A[1] > 0:
        ending_at[1] = A[1]
    for i in range(2,  length - 1):
        if A[i] > 0:
            ending_at[i] = ending_at[i - 1] + A[i]
        else:
            ending_at[i] = ending_at[i - 1]

    starting_from = [0] * length
    reversed_A = A[::-1]
    if reversed_A[1] > 1:
        starting_from[1] = reversed_A[1]
    for i in range(2, length - 1):
        if reversed_A[i] > 0:
            starting_from[i] = starting_from[i - 1] + reversed_A[i]
        else:
            starting_from[i] = starting_from[i - 1]

    starting_from = starting_from[::-1]
    max_double_slice_sum = (0, 0)
    for j in range(1, length - 1):
        summ = ending_at[j - 1] + starting_from[j + 1]
        if summ > max_double_slice_sum[1]:
            max_double_slice_sum = (j, summ)

    return max_double_slice_sum[1]


if __name__ == '__main__':
    unittest.main()
