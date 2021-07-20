# Probably fastest merging method.
def mergeTwoSortedLists(a, b):

    return sorted([*a, *b])