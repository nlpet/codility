"""
Paper on sorting: https://codility.com/media/train/4-Sorting.pdf.

Challenge URL: https://codility.com/demo/take-sample-test/max_product_of_three/
"""
import unittest


class TestMaxTripProd(unittest.TestCase):

    """Unit tests for max product of triples."""

    def tests(self):
        """Tests."""
        self.assertEqual(solution([-3, 1, 2, -2, 5, 6]), 60)
        self.assertEqual(solution([-5, 5, -5, 4]), 125)
        self.assertEqual(solution([-2, -2, 1, 1, 1, 1]), 4)
        self.assertEqual(solution([-5, -6, -4, -7, -10]), -120)


def solution(A):
    """Return max value of any triplet in A."""
    sa = sorted(A)
    fp, lp = sa[0] * sa[1], sa[-3] * sa[-2]
    if fp > lp and sa[-1] > 0:
        return fp * sa[-1]
    else:
        return lp * sa[-1]


if __name__ == '__main__':
    unittest.main()
