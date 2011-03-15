'''
Wikipedia subset sum approximation algorithm
http://en.wikipedia.org/wiki/Subset_sum_problem#Polynomial_time_approximate_algorithm

'''

import operator


def approx_with_accounting_and_duplicates(x_list,
                                s,      # target value
                                ):
    '''
    Modified from http://en.wikipedia.org/wiki/Subset_sum_problem#Polynomial_time_approximate_algorithm

         initialize a list S to contain one element 0.
         for each i from 1 to N do
           let T be a list consisting of xi + y, for all y in S
           let U be the union of T and S
           sort U
           make S empty
           let y be the smallest element of U
           add y to S
           for each element z of U in increasing order do
              //trim the list by eliminating numbers close to one another
              //and throw out elements greater than s
             if y + cs/N < z <= s, set y = z and add z to S
         if S contains a number between (1 - c)s and s, output yes, otherwise no

    '''
    c = .01              # fraction error (constant)
    N = len(x_list)      # number of values

    S = [(0, [])]
    for x in sorted(x_list):
        T = []
        for y, y_list in S:
            T.append((x + y, y_list + [x]))
        U = T + S
        U = sort_by_col(U, 0)
        y, y_list = U[0]
        S = [(y, y_list)]

        for z, z_list in U:
            lower_bound = (float(y) + c * float(s) / float(N))
            if lower_bound < z <= s:
                y = z
                S.append((z, z_list))

    return sort_by_col(S, 0)[-1]


def sort_by_col(table, col=0):
    '''
    http://www.saltycrane.com/blog/2007/12/how-to-sort-table-by-columns-in-python/
    '''
    return sorted(table, key=operator.itemgetter(col))
