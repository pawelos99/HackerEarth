from collections import defaultdict, Counter
from functools import reduce


def factors(n):
    '''returns list of all factors on number n'''
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1)
                       if n % i == 0)))


# read input
N = int(input())
b_bricks = defaultdict(int)
buildings = tuple(int(input()) for _ in range(N))
c_buildings = Counter(buildings)

# for each building calculate all possible brick size
for x, y in c_buildings.items():
    for z in factors(x):
        b_bricks[z] += y

# print result for each query
for _ in range(int(input())):
    print(b_bricks[int(input())])
