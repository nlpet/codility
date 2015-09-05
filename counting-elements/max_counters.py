"""Max counter solution."""
from collections import Counter


def solution(N, A):
    """Solution."""
    l = len(A)
    indices = [x for x in range(l) if A[x] == N + 1]
    if len(indices) == l:
        return [0 for _ in range(N)]
    elif len(indices):
        add = 0
        start = 0
        for i in indices:
            most_common = Counter(
                [x for x in A[start: i + 1] if x != N + 1]
            ).most_common(1)
            if most_common:
                add += most_common[0][1]
            start = i

        counters = [add for _ in range(N)]
        for x in A[indices[-1] + 1:]:
            counters[x - 1] += 1
        return counters
    else:
        counters = [0 for _ in range(N)]
        for x in A:
            counters[x - 1] += 1
        return counters


if __name__ == '__main__':
    N, A = 5, [3, 4, 4, 6, 1, 4, 4]
    print solution(N, A)
