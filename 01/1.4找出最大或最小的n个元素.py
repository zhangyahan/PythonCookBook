import heapq
"""
heapq.nlargest(n, ns):   找出ns数组中最大的n个元素
heapq.nsmallest(n, ns):  找出ns数组中最小的n个元素
"""

ns = [1, 2, 3, 4, 5, 6, 7]

max_nums = heapq.nlargest(2, ns, key=)
min_nums = heapq.nsmallest(2, ns)

print(ns.index(max_nums[0]))
print(min_nums)
