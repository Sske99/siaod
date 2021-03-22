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


def bubble_sort(arr):
    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True


"""
Body program
"""
n, m = 500, 500
a, b = BildArray(n, m)
t = 0
while t != m:
    for j in range(n):
        b[j] = a[t][j]
    bubble_sort(b)
    for j in range(len(b)):
        print("{:4d}".format(b[j]), end="")
    print()
    t += 1

t1 = time.process_time() - t0
print("Time elapsed: ", t1 - t0)
