# coding=utf-8
"""https://codility.com/demo/take-sample-test/genomic_range_query/."""


def solution(S, P, Q):
    """Solution."""
    ifactor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    result = []
    ls = len(S)
    # index 0 = A, 1 = C, 2 = G, 3 = T
    pos = [[-1]*ls for _ in range(4)]
    pos[ifactor[S[-1]] - 1][-1] = ls - 1
    for i in range(ls - 2, -1, -1):
        pos[0][i] = pos[0][i+1]
        pos[1][i] = pos[1][i+1]
        pos[2][i] = pos[2][i+1]
        pos[3][i] = pos[3][i+1]
        pos[ifactor[S[i]] - 1][i] = i

    for j in range(len(P)):
        if pos[0][P[j]] != -1 and pos[0][P[j]] <= Q[j]:
            result.append(1)
        elif pos[1][P[j]] != -1 and pos[1][P[j]] <= Q[j]:
            result.append(2)
        elif pos[2][P[j]] != -1 and pos[2][P[j]] <= Q[j]:
            result.append(3)
        else:
            result.append(4)
    return result


if __name__ == '__main__':
    s, p, q = 'CAGCCTA', [2, 5, 0], [4, 5, 6]
    print(solution(s, p, q))
