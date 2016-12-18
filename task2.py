import random
import numpy as np
import matplotlib.pyplot as plt
from math import *

number_of_iteration = 100000

def monte_carlo(function, square) :
    x = []
    y = []
    under_function = 0
    for number in range(1 + number_of_iteration):
        rand_x = random.random() * 1
        rand_y = random.random() * function(1)
        x.append(rand_x)
        y.append(rand_y)
        if y[number] <= function(x):
            under_function +=1
    return (under_function / number_of_iteration) / square


def first_function(x):
    return pow(x, 7) + pow(x, 5) + pow(x, 3)
First = monte_carlo(first_function, first_function(1))
print('Function (x^7 + x^5 + x^3)dx from 0 to 1')
print('Integral 1 = ', First)


print('Function 2sin(3x)dx from 0 to pi')

in_x = pi
in_y = 2 * sin(pi / 2)
square = in_x * in_y

x = []
y = []
under_function = 0

for number in range(1 + number_of_iteration):
    rand_x = random.random() * in_x
    rand_y = random.random() * in_y
    x.append(rand_x)
    y.append(rand_y)
    if y[number] <= (2 * sin(3 * x[number])):
        under_function += 1
square_a = (under_function / number_of_iteration)

under_function = 0
x = []
y = []

for number in range(1 + number_of_iteration):
    rand_x = random.random() * in_x
    rand_y = random.random() * -in_y
    x.append(rand_x)
    y.append(rand_y)
    if y[number] >= (2 * sin(3 * x[number])):
        under_function += 1

square_b = (under_function / number_of_iteration)
square2 = square_a - square_b
Second = square2 * square
print('Integral 2 = ', Second)

print('Function 1/((x + 1) * sqrt(x)) dx from 0 to infinity')

x = [np.random.uniform(0.0001, 1) for i in range(number_of_iteration)]
sum_1 = 0
for element in x:
    sum_1 += 1 / ((element + 1) * sqrt(element))
int_sum_1 = (1.0 / number_of_iteration) * sum_1

x = [np.random.uniform(1, 100) for i in range(number_of_iteration)]
sum_2 = 0
for element in x:
    sum_2 += 1 / ((element + 1) * sqrt(element))
int_sum_2 = (99.0 / number_of_iteration) * sum_2

x = [np.random.uniform(100, 5000) for i in range(number_of_iteration)]
sum_3 = 0
for element in x:
    sum_3 += 1 / ((element + 1) * sqrt(element))
int_sum_3 = (4900.0 / number_of_iteration) * sum_3

Third = int_sum_1 + int_sum_2 + int_sum_3

print('Integral 3 = ', Third)

x = np.arange(0, 1, .02)
y = np.power(x, 7) + np.power(x, 5) + np.power(x, 3)
x2 = np.arange(0, np.pi, .02)
y2 = 2 * np.sin(3 * x2)
x3 = np.arange(10 ** -3, 3, .002)
y3 = 1 / ((x3 + 1) * np.sqrt(x3))

f, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(x, y, 'r--', label=round(First, 4))
ax1.legend(loc='upper right')

ax2.plot(x2, y2, 'r--', label=round(Second, 4))
ax2.legend(loc='lower right')

ax3.plot(x3, y3, 'r--', label=round(Third, 4))
ax3.legend(loc='upper right')

plt.show()
