from AVLTree import *
import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
t = None
for i in range(n):
    op, key = input().split()
    key = int(key)
    if op == 'I':
        t = insert(t, key, None)
    if op == 'D':
        t = remove(t, key)
    if op == 'K':
        x = kth(t, key)
        print("invalid" if x is None else x.key)
    if op == 'C':
        print(count_less(t, key))
