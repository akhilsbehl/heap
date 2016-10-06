'''Implements a running median calculator.'''


from heap import Heap


def _median(smallers, largers):
    if smallers.size == largers.size:
        return (smallers.root + largers.root) / 2
    elif smallers.size < largers.size:
        return float(largers.root)
    else:
        return float(smallers.root)


def running_median(stream):
    smallers, largers, i = Heap([], "max"), Heap([], "min"), 2
    smallers.push(min(stream[0:2]))
    largers.push(max(stream[0:2]))
    yield float(stream[0])
    median = (stream[0] + stream[1]) / 2.
    yield median
    while i < len(stream):
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
    INPUT = [12, 4, 5, 3, 8, 7]
    OUTPUT = [12., 8., 5., 4.5, 5., 6.]
    assert list(running_median(INPUT)) == OUTPUT
