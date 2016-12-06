#! /usr/bin/env python

import random
import timeit

TEST_LIST_SIZE = 10000

def generate_random_list(size):
    return random.sample(xrange(size), size)

def naive_simple(l):
    a = []
    b = []
    for i in l:
        if i % 100 == 0:
            a.append(i)
        if i % 200 == 0:
            b.append(i)
    return a, b

def naive_smart(l):
    a = []
    b = []
    for i in l:
        if i % 100 == 0:
            a.append(i)
            if i % 200 == 0:
                b.append(i)
    return a, b

def filter_single(l, n):
    return [i for i in l if i % n == 0]

def filter_multiple(l, list_n):
    return [
        [i for i in l if i % n == 0] for n in list_n
    ]

def filter_lambda_single(l, n):
    return filter(lambda x: x % n == 0, l)

def naive_simple_test():
    l = generate_random_list(TEST_LIST_SIZE)
    a, b = naive_simple(l)

def naive_smart_test():
    l = generate_random_list(TEST_LIST_SIZE)
    a1, b1 = naive_smart(l)

def filter_single_test():
    l = generate_random_list(TEST_LIST_SIZE)
    a2, b2 = filter_single(l, 100), filter_single(l, 200)

def filter_multiple_test():
    l = generate_random_list(TEST_LIST_SIZE)
    a3, b3 = filter_multiple(l, [100,200])

def filter_lambda_single_test():
    l = generate_random_list(TEST_LIST_SIZE)
    a4, b4 = filter_lambda_single(l, 100), filter_lambda_single(l, 200)

if __name__ == '__main__':
    l = generate_random_list(TEST_LIST_SIZE)

    a, b = naive_simple(l)

    a1, b1 = naive_smart(l)

    a2, b2 = filter_single(l, 100), filter_single(l, 200)

    a3, b3 = filter_multiple(l, [100,200])

    a4, b4 = filter_lambda_single(l, 100), filter_lambda_single(l, 200)

    print a == a1
    print b == b1

    print a1 == a2
    print b1 == b2

    print a2 == a3
    print b2 == b3

    print a3 == a4
    print b3 == b4

    print 'Array generation', timeit.timeit('generate_random_list(TEST_LIST_SIZE)', 'from __main__ import generate_random_list, TEST_LIST_SIZE', number=10000)
    print 'Naive simple', timeit.timeit('naive_simple_test()', 'from __main__ import naive_simple_test', number=10000)
    print 'Naive smart', timeit.timeit('naive_smart_test()', 'from __main__ import naive_smart_test', number=10000)
    print 'Filter single', timeit.timeit('filter_single_test()', 'from __main__ import filter_single_test', number=10000)
    print 'Filter multiple', timeit.timeit('filter_multiple_test()', 'from __main__ import filter_multiple_test', number=10000)
    print 'Filter lambda single', timeit.timeit('filter_lambda_single_test()', 'from __main__ import filter_lambda_single_test', number=10000)
