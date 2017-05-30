import operator


def solution_asc(dic):
    """
    Sorts given dictionary by keys in ascending order.

    Returns tuple of sorted (value, key)
    """
    return sorted(dic.iteritems(), key=operator.itemgetter(0))


def solution_desc(dic):
    """
    Sorts given dictionary by values in descending order.

    Returns tuple of sorted (value, key)
    """
    return sorted(dic.iteritems(), key=operator.itemgetter(0), reverse=True)


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(solution_asc(d))
