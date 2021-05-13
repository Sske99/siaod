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


def sel_sort(array):
    for i in range(len(array) - 1):
        k = i
        j = i + 1
        while j < len(array):
            if array[j] < array[k]:
                k = j
            j = j + 1
        array[i], array[k] = array[k], array[i]


"""
Body program
"""
n, m = 500, 500

a, b = BildArray(n, m)
t = 0
while t != m:
    for j in range(n):
        b[j] = a[t][j]
    sel_sort(b)
    for j in range(len(b)):
        print("{:4d}".format(b[j]), end="")
    print()
    t += 1

t1 = time.process_time() - t0
print("Time elapsed: ", t1 - t0)
