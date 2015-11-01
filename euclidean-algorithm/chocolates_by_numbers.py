"""https://codility.com/programmers/task/chocolates_by_numbers"""


def solution(N, M):
    chocolates = [False] * N
    i = 0
    count = 0
    while not chocolates[i]:
        chocolates[i] = True
        i = (i + M) % N
        count += 1
    return count


if __name__ == '__main__':
    N, M = 10, 4
    print(solution(N, M))
