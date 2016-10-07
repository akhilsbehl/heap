'''Implements heapsort.'''


import random
from heap import Heap


def heapsort(array, increasing=True):
    '''Implements sorting using heaps.'''
    order = {True: 'min', False: 'max'}[increasing]
    heap = Heap(array, order)
    sorted_array = []
    while heap.data:
        sorted_array.append(heap.pop())
    return sorted_array


if __name__ == '__main__':
    SIZE = int(random.uniform(0, 100))
    SAMPLE = list(set(int(random.uniform(1, 100)) for x in range(SIZE)))
    assert heapsort(SAMPLE) == sorted(SAMPLE)
    assert heapsort(SAMPLE, increasing=False) == sorted(SAMPLE, reverse=True)
    print('All tests passed! :)')
