import numpy
import matplotlib.pyplot as plt

A = [x for x in range(10)]
B = [a ** 2 for a in A if a % 2 == 0]
print(B)
plt.plot(B)
plt.show()
