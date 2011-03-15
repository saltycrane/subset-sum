'''
Results:

Brute force: (8270, (75, 3265, 2145, 1935, 850)) 231.761588812
Stackoverflow: (8270, [1150, 495, 995, 995, 995, 995, 100, 750, 75, 140, 140, 1330, 110]) 0.0585901737213
Hetland: 8270 0.264632940292
Wikipedia: (8270, [15, 75, 140, 140, 1330, 3265, 3305]) 0.101099967957

'''

from time import time

import bruteforce
import stackoverflow
import hetland
import wikipedia


def main():
    # x_list = [100, 75, 15, 495, 995, 995, 995, 995, 510, 110]
    # target = 635
    x_list = [1150, 495, 995, 995, 995, 995, 100, 750, 3305, 75, 510, 3265, 2145, 1935, 140, 140, 15, 1330, 2800, 1250, 350, 850, 110]
    target = 8270

    time0 = time()
    bf = bruteforce.bruteforce(x_list, target)
    time1 = time()
    so = stackoverflow.stackoverflow(x_list, target)
    time2 = time()
    he = hetland.bb_knapsack(x_list, target)
    time3 = time()
    wi = wikipedia.approx_with_accounting_and_duplicates(x_list, target)
    time4 = time()

    print 'Brute force:', bf, time1 - time0
    print 'Stackoverflow:', so, time2 - time1
    print 'Hetland:', he, time3 - time2
    print 'Wikipedia:', wi, time4 - time3


if __name__ == '__main__':
    main()
