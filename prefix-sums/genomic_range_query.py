# coding=utf-8
u"""Genomic range query."""


def solution(S, P, Q):
    """Solution."""
    ifs = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }
    irs = {}
    S = [ifs[c] for c in S]
    indices = zip(P, Q)
    results = []
    for i, j in indices:
        if [(i, j)] in irs.keys():
            mmin = irs[(i, j)]
        else:
            mmin = min(set(S[i:j+1]))
            irs[(i, j)] = mmin
        results.append(mmin)
    return results
