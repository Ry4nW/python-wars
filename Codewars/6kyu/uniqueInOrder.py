from typing import Iterable


def unique_in_order(iterable):

    uniqueList = []
    prev = ''

    for i in iterable:

        if i != prev:
            prev = i
            uniqueList.append(i)
    
    return uniqueList

# One-liner:

def unique_in_order2(iterable):

    return [iterable[i] for i in range(len(iterable)) if iterable[i - 1] != iterable[i] or i == 0]




