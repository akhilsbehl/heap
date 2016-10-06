'''Implements heapsort.'''


from heap import Heap


def heapsort(array, increasing=True):
    order = {True: 'min', False: 'max'}[increasing]
    heap = Heap(array, order)
    sorted_array = []
    while heap.data:
        sorted_array.append(heap.pop())
    return sorted_array
