"""
https://codility.com/programmers/task/max_profit
"""


def maximal_subarray(array, n):
    """

    :list : array
    """
    if min(array) >= 0:
        return sum(array)
    if max(array) <= 0:
        return 0

    current_sum, max_sum = 0, 0
    for i in range(n):
        current_sum = max(current_sum + array[i], 0)
        max_sum = max(max_sum, current_sum)
    return max_sum


def solution(array):
    """
    :list : array
    """
    n = len(array)
    if n == 0:
        return 0
    days_deltas = [0 for _ in range(n)]
    for i in range(1, n):
        days_deltas[i] = array[i] - array[i - 1]

    max_profit = maximal_subarray(days_deltas, n)
    return max_profit


if __name__ == '__main__':
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    print solution(A)
