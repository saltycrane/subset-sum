import itertools

from decorators import timeout


@timeout(5 * 60)
def bruteforce(x_list, target):
    possiblities = []
    for x in powerset(x_list):
        possiblities.append((x, sum(x)))

    x_list, actual_value = closest(possiblities, target)

    return (actual_value, x_list)


def powerset(iterable):
    '''powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    http://docs.python.org/library/itertools.html#recipes
    '''
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def closest(possiblities, target):
    '''Modified from http://stackoverflow.com/questions/445782/finding-closest-match-in-collection-of-numbers/445824#445824'''
    return min((abs(target - total), (o_list, total))
               for o_list, total in possiblities)[1]
