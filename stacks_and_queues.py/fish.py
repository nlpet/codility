"""
https://codility.com/demo/take-sample-test/fish/

Given two arrays A and B, where A contains the fish sizes and
B contains the directions in which the fish are swimming (0 = upstream).
When two fish meet, the bigger one eats the smaller one. Find the number
of fish that are alive in the end.
"""

class Queue(object):
    """
    Queue object for managing downstream / upstream fish.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item, index):
        self.queue.append((item, index))

    def dequeue(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return ' '.join([str(n) for n in self.queue])


def solution(A, B):
    """
    :list : A
    :list : B
    """
    upstream, downstream = Queue(), Queue()
    for i in range(len(A)):
        # If fish is flowing downstream
        if B[i]:
            downstream.enqueue(A[i])
            # Fish A[i] meets all the fish from the upstream queue
            while len(upstream) and len(downstream):
                fish_size, fish_index = upstream.peek()
                if fish_index > i:
                    if A[i] > fish_size:
                        upstream.dequeue()
                    else:
                        downstream.dequeue()
        # If fish is flowing upstream
        else:
            upstream.enqueue(A[i])
            # Fish A[i] meets all the fish from the downstream queue
            while len(downstream) and len(upstream):
                fish_size, fish_index = downstream.peek()
                if fish_index < i:
                    if A[i] > fish_size:
                        downstream.dequeue()
                    else:
                        upstream.dequeue()
    return sum(len(upstream) + len(downstream))


if __name__ == '__main__':
    A = [4, 3, 2, 1, 5]
    B = [0, 1, 0, 0, 0]
    print "Fish left alive %d" % solution(A, B)
