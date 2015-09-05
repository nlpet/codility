"""Perm missing elements."""


def solution(A):
    """Solution."""
    lookup = {x: 1 for x in range(1, len(A)+2)}
    for n in A:
        lookup.pop(n, None)
    return lookup.popitem()[0]
