import random

ITERATIONS_COUNT = 10000
randList = [random.random() for _ in xrange(ITERATIONS_COUNT)]
maxRand = max(randList)
minRand = min(randList)
R = maxRand - minRand
K = 7.0
n = R/K
t = 1.0 / K
H = R
randList.sort()

for i in range(0, int(K) - 1):
    A = minRand + n * i
    B = maxRand + n * (i + 1)
    if B == maxRand:
        S = len([val for val in randList if A <= val <= B])
    else:
        S = len([val for val in randList if A <= val < B])
    H += (((t - S / ITERATIONS_COUNT) * (t - S / ITERATIONS_COUNT)) / t)

print H
