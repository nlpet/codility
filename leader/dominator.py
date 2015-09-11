"""
Chapter readings: https://codility.com/media/train/6-Leader.pdf
Problem URL: https://codility.com/demo/take-sample-test/dominator/
"""
from collections import defaultdict


def solution(A):
    doms = defaultdict(int)
    dom = [0, 0]
    for i in range(len(A)):
        doms[A[i]] += 1
        if doms[A[i]] > dom[0]:
            dom = (doms[A[i]], i)
    if dom[0] > len(A) / 2.:
        return dom[1]
    return -1


if __name__ == '__main__':
    A = [3, 4, 3, 2 ,3 , -1, 3, 3]
    print solution(A)
