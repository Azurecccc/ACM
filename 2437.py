import sys
sys.setrecursionlimit(3000)
func_recored = [-1] * 2000

def func(n, m):
    if n < m:
        return 0
    if n == m:
        return 1
    if func_recored[n] != -1:
        return func_recored[n]
    func_recored[n] = func(n - 1, m) + func(n - 2, m)
    return func_recored[n]

m, n = [int(x) for x in input().split()]
print(func(n, m))
