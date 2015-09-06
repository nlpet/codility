"""https://codility.com/demo/take-sample-test/brackets/"""
import unittest


class TestBrackets(unittest.TestCase):

    """Unit tests for max product of triples."""

    def tests(self):
        """Tests."""
        self.assertEqual(solution(''), 1)
        self.assertEqual(solution('{[()()]}'), 1)
        self.assertEqual(solution('([)()]'), 0)
        self.assertEqual(solution('{{{{}}}}'), 1)
        self.assertEqual(solution('{{[][]([[[]]])}}'), 1)
        self.assertEqual(solution('[[[[{]]]]'), 0)
        self.assertEqual(solution(')('), 0)


class Stack(object):

    """Stack implementation."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def pop(self):
        """Remove the last item from the stack if not empty and return it."""
        if self.stack:
            return self.stack.pop()
        return None

    def add(self, item):
        """Add item to the stack."""
        self.stack.append(item)

    def __str__(self):
        """Return the items in the stack separated by space."""
        return ' '.join(self.stack)

    def peek(self):
        """Get the last item from the stack."""
        if self.stack:
            return self.stack[-1]
        return None

    def __len__(self):
        """Return length of stack."""
        return len(self.stack)


def solution(S):
    """Return 1 if string is properly nested, else 0."""
    if not len(S):
        return 1

    stack = Stack()
    for c in S:
        if c in ['[', '(', '{']:
            stack.add(c)
        elif c == ')' and stack.peek() == '(':
            stack.pop()
        elif c == ']' and stack.peek() == '[':
            stack.pop()
        elif c == '}' and stack.peek() == '{':
            stack.pop()
        else:
            return 0
    if not len(stack):
        return 1
    return 0


if __name__ == '__main__':
    unittest.main()
