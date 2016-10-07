'''Implements a running median calculator.'''


import random
import statistics
from heap import Heap


def _median(smallers, largers):
    if smallers.size == largers.size:
        return (smallers.root + largers.root) / 2
    elif smallers.size < largers.size:
        return float(largers.root)
    else:
        return float(smallers.root)


def running_median(stream):
    '''Compute the running median on a stream. Adopt for an appropriate
    stream type.'''
    smallers, largers, i = Heap([], "max"), Heap([], "min"), 2
    smallers.push(min(stream[0:2]))
    largers.push(max(stream[0:2]))
    yield float(stream[0])
    median = (stream[0] + stream[1]) / 2.
    yield median
    while i < len(stream):
        # pylint: disable=expression-not-assigned
        smallers.push(stream[i]) if \
            stream[i] < smallers.root else \
            largers.push(stream[i])
        if smallers.size > largers.size:
            largers.push(smallers.pop())
        elif largers.size > smallers.size:
            smallers.push(largers.pop())
        median = _median(smallers, largers)
        yield median
        i += 1


if __name__ == '__main__':
    SIZE = int(random.uniform(0, 50))
    SAMPLE = list(set(int(random.uniform(1, 100)) for x in range(SIZE)))
    RM = running_median(SAMPLE)
    for n in range(1, len(SAMPLE) + 1):
        assert next(RM) == statistics.median(SAMPLE[:n])
    print("All tests passed! :)")
