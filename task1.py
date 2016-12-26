import random
import math

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
    H += ((t - S / ITERATIONS_COUNT) ** 2) / t

print H

Mat = sum(randList)/ITERATIONS_COUNT
Disp = 0
G = 0


def xk(n, m):
    rand_list = [random.uniform(0, 1) for i in range(n)]
    inter_list = [[] for i in range(m)]
    sum = 0
    s = 1.0
    i = 0
    expected = (1.0 / m) * n
    while s <= m:
        for element in rand_list:
            if (element <= (s / m)) and (element > ((s - 1) / m)):
                inter_list[i].append(element)
        s += 1
        i += 1

    for element in inter_list:
        sum += ((len(element) - expected) ** 2) / (n * expected)
    return sum


print('Mat : ', Mat)

for i in range(ITERATIONS_COUNT):
    Disp += ((randList[i] - Mat)**2/ITERATIONS_COUNT)

print('Disp : ', Disp)
print('G : ', math.sqrt(Disp))
print('Xi^2 : ', xk(ITERATIONS_COUNT, int(math.ceil(H))))




