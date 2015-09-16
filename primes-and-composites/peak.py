"""
A peak is defined as an element which is larger than both of its
neighbors. Given a non-empty array A of N integers, find the max
number of blocks into which the array can be divided such that
each block contains at least 1 peak.
"""


def solution(A):
    peaks_indices = []
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks_indices.append((i, A[i]))
    return peaks_indices




if __name__ == '__main__':
    A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
    print solution(A)
