'''
http://search.safaribooksonline.com/book/programming/python/9781430232377/hard-problems-and-limited-sloppiness/when_the_going_gets_tough_comma_the_smar

'''

from __future__ import division
from heapq import heappush, heappop
from itertools import count


def bb_knapsack(v, c):
    sol = [0]                                     # Solution so far (global var)
    n = len(v)                                    # Item count

    idxs = list(range(n))

    def bound(sv, m):                             # Greedy knapsack bound
        if m == n:
            return sv                             # No more items?
        objs = ((v[i], 'dum') for i in idxs[m:])  # Descending unit cost order
        for av, _ in objs:                        # Added value and weight
            if sv + av > c:
                break                             # Still room?
            sv += av                              # Add val to sum of vals
        return sv + (c - sv)                      # Add fraction of last item

    def node(sv, m):                              # A node (generates children)
        if sv > c:
            return                                # Weight sum too large? Done
        sol[0] = max(sol[0], sv)                  # Otherwise: Update solution
        if m == n:
            return                                # No more objects? Return
        i = idxs[m]                               # Get the right index
        ch = [('dum', sv), ('dum', sv + v[i])]    # Children: without/with m
        for _, sv in ch:                          # Try both possibilities
            b = bound(sv, m + 1)                  # Bound for m+1 items
            if b > sol[0]:                        # Is the branch promising?
                yield b, node(sv, m + 1)          # Yield child w/bound

    num = count()                                 # Helps avoid heap collisions
    Q = [(0, next(num), node(0, 0))]              # Start with just the root
    while Q:                                      # Any nodes left?
        _, _, r = heappop(Q)                      # Get one
        for b, u in r:                            # Expand it ...
            heappush(Q, (b, next(num), u))        # ... and push the children

    return sol[0]                                 # Return the solution
