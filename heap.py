'''Implements a heap.'''


import operator
import random


class Heap(object):
    '''Implements a heap. May not work when data has duplicates.'''

    def __init__(self, iterable, order="max"):
        self.order = order
        self.comparator = {"min": operator.lt, "max": operator.gt}[self.order]
        self.data = list(iterable)
        for pos in range((self.size - 2) // 2, -1, -1):
            # These are the non-leaf positions
            self.fix(pos)

    @property
    def size(self):
        '''Returns the current size of the heap'''
        return len(self.data)

    def fix(self, pos):
        '''Fix the heap with one invalid entry to obtain the heap
        invariant.'''
        if pos > ((self.size - 2) // 2):  # These are leaves again
            return None
        left, right = 2 * pos + 1, 2 * pos + 2
        if right == self.size:  # The root with only a left leaf
            if self.comparator(self.data[left], self.data[pos]):
                self.data[pos], self.data[left] = \
                    self.data[left], self.data[pos]
            return None
        if self.comparator(self.data[pos], self.data[left]) and \
           self.comparator(self.data[pos], self.data[right]):
            return None
        swap = left if self.comparator(self.data[left],
                                       self.data[right]) else right
        self.data[pos], self.data[swap] = self.data[swap], self.data[pos]
        self.fix(swap)

    @property
    def root(self):
        '''Gives the value at the heap's root.'''
        if self.data:
            return self.data[0]

    def pop(self):
        '''Consumes the value at the heap's root and fixs for the
        invariant.'''
        if self.size >= 2:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            popped = self.data.pop()
            self.fix(0)
            return popped
        return self.data.pop(0)  # Raises the correct error.

    def push(self, elem):
        '''Pushes an element in to the heap and fixs for the invariant.'''
        self.data.insert(0, elem)
        self.fix(0)

    @staticmethod
    def is_heap(iterable, order="max"):
        '''Checks if a given iterable satisfies the heap invariant.
           NB: Will consume your iterable.'''
        comparator = {"min": operator.lt, "max": operator.gt}[order]
        for pos in range(0, (len(iterable) - 2) // 2):
            this = iterable[pos]
            left, right = iterable[2 * pos + 1], iterable[2 * pos + 2]
            if not (comparator(this, left) and comparator(this, right)):
                return False
        return True

    def is_valid(self):
        '''Checks if the data still satisfies the heap invariant.'''
        return self.is_heap(self.data, self.order)

    def __repr__(self):
        return repr(self.data)


if __name__ == "__main__":

    SIZE = int(random.uniform(1, 10))
    SAMPLE = list(set([int(random.uniform(1, 1000)) for x in range(SIZE)]))

    MAX_HEAP = Heap(SAMPLE, "max")
    MIN_HEAP = Heap(SAMPLE, "min")

    assert MAX_HEAP.is_valid()
    assert MIN_HEAP.is_valid()

    DATA = MAX_HEAP.data
    MAX_HEAP.fix(0)  # Should do nothing.
    assert MAX_HEAP.data == DATA

    DATA = MIN_HEAP.data
    MIN_HEAP.fix(0)  # Should do nothing.
    assert MIN_HEAP.data == DATA

    SAMPLE_MAX = max(SAMPLE)
    assert MAX_HEAP.root == SAMPLE_MAX
    assert MAX_HEAP.pop() == SAMPLE_MAX
    assert MAX_HEAP.is_valid()

    SAMPLE_MIN = min(SAMPLE)
    assert MIN_HEAP.root == SAMPLE_MIN
    assert MIN_HEAP.pop() == SAMPLE_MIN
    assert MIN_HEAP.is_valid()

    MAX_HEAP.push(SAMPLE_MAX)
    assert MAX_HEAP.root == SAMPLE_MAX

    MIN_HEAP.push(SAMPLE_MIN)
    assert MIN_HEAP.root == SAMPLE_MIN

    print("All checks passed! :)")
