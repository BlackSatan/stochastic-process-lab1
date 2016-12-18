import random
import matplotlib.pyplot as plt

ITERATIONS_COUNT = 100
uniformDistributionList = []
for i in xrange(ITERATIONS_COUNT):
    uniformDistributionList.append(max([random.random() for _ in xrange(ITERATIONS_COUNT)]))

plt.subplot(2, 1, 2)
plt.hist(uniformDistributionList, 25)
plt.show()
