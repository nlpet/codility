"""
https://codility.com/demo/take-sample-test/equi_leader/
"""


def solution(A):
    doms = {}
    dom = [0, 0]
    length = len(A)
    for i in range(length):
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
    # Number of leadrs in the first half
    fst = 0
    # Number of leaders in the second half
    snd = leader[0]

    solutions = 0

    for i in leader[1]:
        fst += 1
        snd -= 1
        # Number of non-leaders in the first half
        fst_non = (i + 1) - fst
        # Number of non-leaders in the second half
        snd_non = length - (i + 1) - snd
        if fst > fst_non and snd > snd_non:
            solutions += 1
    return solutions


if __name__ == '__main__':
    A = [4, 3, 4, 4, 4, 2]
    print solution(A)
