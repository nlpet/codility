"""Perm check solution."""


def solution(A):
    """Solution."""
    unvisited = set([x for x in range(1, len(A) + 1)])
    for n in A:
        try:
            unvisited.remove(n)
        except KeyError:
            return 0
    if len(unvisited) == 0:
        return 1
    return 0
