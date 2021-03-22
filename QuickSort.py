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


def QuickSort(a, first, last):
    if first >= last:
        return
    m = a[(last + first) // 2]
    b, e = first, last
    while b <= e:
        while a[b] < m:
            b = b + 1
        while a[e] > m:
            e = e - 1
        if b <= e:
            a[b], a[e] = a[e], a[b]
            b, e = b + 1, e - 1
    QuickSort(a, first, e)
    QuickSort(a, b, last)


"""
Body program
"""
n, m = 500, 500

a, b = BildArray(n, m)
t = 0
while t != m:
    for j in range(n):
        b[j] = a[t][j]
    QuickSort(b, 0, len(b) - 1)
    for j in range(len(b)):
        print("{:4d}".format(b[j]), end="")
    print()
    t += 1

t1 = time.process_time() - t0
print("Time elapsed: ", t1 - t0)
