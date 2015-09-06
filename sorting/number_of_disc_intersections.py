"""https://codility.com/demo/take-sample-test/number_of_disc_intersections/"""


def solution(A):
    """Return number of overlapping circles in a plane."""
    N = len(A)
    pairs = []
    for j in range(N):
        start = max(0, j - A[j])
        end = min(N - 1, j + A[j])
        pairs.append((start, end))
    # TO DO - find overlapping pairs
    return pairs

solution([1, 5, 2, 1, 4, 0])
