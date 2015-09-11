"""
https://codility.com/demo/take-sample-test/fish/

Given two arrays A and B, where A contains the fish sizes and
B contains the directions in which the fish are swimming (0 = upstream).
When two fish meet, the bigger one eats the smaller one. Find the number
of fish that are alive in the end.
"""


def solution(A, B):
    survived = 0
    downstream = []

    for i in range(len(A)):
        if B[i] == 1:
            downstream.append(A[i])
        else:
            while len(downstream) != 0:
                if downstream[-1] < A[i]:
                    downstream.pop()
                else:
                    break
            else:
                survived += 1
    return len(downstream) + survived


if __name__ == '__main__':
    A = [4, 3, 2, 1, 5]
    B = [0, 1, 0, 0, 0]
    print "Fish left alive %d" % solution(A, B)
