from RedBlackTree import *
import sys

from btrees.AbstractTree import count_less, kth

sys.setrecursionlimit(10 ** 6)

n = int(input())
t = Tree()
for i in range(n):
    op, key = input().split()
    key = int(key)
    if op == 'I':
        t = insert(t, key, None)
        show(t)
    if op == 'D':
        t = remove(t, key)
    if op == 'K':
        x = kth(t, key)
        print("invalid" if x is None else x.key)
    if op == 'C':
        print(count_less(t, key))