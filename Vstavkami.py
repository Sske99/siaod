from random import randint
import time

t0 = time.process_time()

"""
Method arrays
"""


def BildArray(n, m):
    c = [[randint(100, 999) for j in range(m)] for i in range(n)]

    d = [0] * m

    return c, d


"""
Method sort
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp


"""
Body program
"""
n, m = 500, 500

a, b = BildArray(n, m)
t = 0
while t != m:
    for j in range(n):
        b[j] = a[t][j]
    insertion_sort(b)
    for j in range(len(b)):
        print("{:4d}".format(b[j]), end="")
    print()
    t += 1

t1 = time.process_time() - t0
print("Time elapsed: ", t1 - t0)
