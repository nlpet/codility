"""https://codility.com/demo/take-sample-test/triangle/"""


def solution(A):
    """Return 1 if there exists a triangular triplet, else 0"""
    la = len(A)
    if la < 3:
        return 0

    A.sort()

    for i in range(la - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0
