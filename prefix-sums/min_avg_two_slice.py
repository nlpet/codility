# coding=utf-8
u"""Min avg two slice solution."""


def solution(A):
    """Solution."""
    min_avg_slice = sum(A[0:2]) / 2.0
    min_avg_indx = 0
    l = len(A)

    for i in range(0, l-2):
        current_avg_two = (A[i] + A[i+1]) / 2.0
        current_avg_three = (A[i] + A[i+1] + A[i+2]) / 3.0

        if current_avg_two < min_avg_slice:
            min_avg_slice = current_avg_two
            min_avg_indx = i

        if current_avg_three < min_avg_slice:
            min_avg_slice = current_avg_three
            min_avg_indx = i

    last_avg_two = (A[-2] + A[-1]) / 2.0
    if last_avg_two < min_avg_slice:
        min_avg_slice = last_avg_two
        min_avg_indx = l-2

    return min_avg_indx
