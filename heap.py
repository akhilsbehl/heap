'''Implements a heap.'''


class heap(object):
    '''Implements a heap.'''

    def __init__(self, iterable):
        heap = list(iterable)
        size = len(heap)
        for i in range(size // 2, 0, -1):
            self.correct(heap, i)

    def correct(self, i):
        if i >= (self.size // 2):
            return None
        li, ri = 2 * i + 1, 2 * i + 2
        this, left, right = self.heap[i], self.heap[li], self.heap[ri]
        if self.heap[i] > self.heap[li] and \
           self.heap[i] > self.heap[ri]:
            return None
        i_ = li if self.heap[li] > self.heap[ri] else ri
        self.heap[i], self.heap[i_] = self.heap[i_], self.heap[i]
        self.correct(i_)

    def peek(self):
        return self.heap[0]

    def pop(self):
        pass

    @property
    def push(self, elem):
        pass
