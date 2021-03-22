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


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


"""
Body program
"""
n, m = 500, 500

a, b = BildArray(n, m)
t = 0
while t != m:
    for j in range(n):
        b[j] = a[t][j]
    heap_sort(b)
    for j in range(len(b)):
        print("{:4d}".format(b[j]), end="")
    print()
    t += 1

t1 = time.process_time() - t0
print("Time elapsed: ", t1 - t0)
