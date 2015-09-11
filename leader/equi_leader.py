"""
https://codility.com/demo/take-sample-test/equi_leader/
"""


def solution(A):
    doms = {}
    dom = [0, 0]
    for i in range(len(A)):
        try:
            doms[A[i]][0] += 1
            doms[A[i]][1].append(i)
            doms[A[i]][2] += 1
            if doms[A[i]][2] > dom[0]:
                dom[0] = A[i]
                dom[1] = doms[A[i]][2]
        except (KeyError, IndexError):
            doms[A[i]] = [1, [i], 1]

    leader = doms[dom[0]]
    return leader


if __name__ == '__main__':
    A = [4, 3, 4, 4, 4, 2]
    print solution(A)
