"""
https://codility.com/demo/take-sample-test/equi_leader/
"""
import unittest


class TestEquiLeader(unittest.TestCase):

    """Unit tests for max product of triples."""

    def tests(self):
        """Tests."""
        self.assertEqual(solution([1, 2]), 0)
        self.assertEqual(solution([0]), 0)
        self.assertEqual(solution([4, 3, 4, 4, 4, 2]), 2)
        self.assertEqual(solution([4, 4, 2, 5, 3, 4, 4, 4]), 3)


def solution(A):
    dom = 0
    count = 0
    N = len(A)

    for i in range(N):
        if count == 0:
            dom = i
        if A[i] == A[dom]:
            count += 1
        else:
            count -= 1

    count = len([i for i in range(N) if A[i] == A[dom]])
    if count <= (N / 2):
        return 0

    leader = A[dom]
    equis = 0
    first_half, second_half = 0, count

    for j in range(N):
        if A[j] == leader:
            first_half += 1
            second_half -= 1

        if first_half > (j + 1) / 2 and second_half > (N - j - 1) / 2:
            equis += 1

    return equis


if __name__ == '__main__':
    unittest.main()
