"""https://codility.com/demo/take-sample-test/stone_wall/

         _
 _ _    |_|_     _
|   |  _|_ _|_  | |
|   | |       | | |
|_ _|_|_ _ _ _| | |
|             |_|_|
|             |   |
|             |   |
|_ _ _ _ _ _ _|_ _|

"""


def solution(H):
    """Returns minimum number of blocks needed to build the wall H."""
    stack = []
    blocks = 0

    for h in H:
        while len(stack) and h < stack[-1]:
            stack.pop()
            blocks += 1

        if not len(stack) or h > stack[-1]:
            stack.append(h)

    blocks += len(stack)
    return blocks


if __name__ == '__main__':
    print solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
