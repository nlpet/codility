"""https://codility.com/demo/take-sample-test/frog_jmp/."""


def solution(X, Y, D):
    """Solution."""
    if X == Y:
        return 0
    div, remainder = divmod(Y - X, D)
    if remainder:
        div += 1
    return div
