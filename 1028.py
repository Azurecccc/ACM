import sys
sys.setrecursionlimit(3000)
func_recored = [-1] * 2000

def func(n):
    if n == 1:
        return 1
    if func_recored[n] != -1:
        return func_recored[n]
    func_recored[n] = 1
    for i in range(1, n // 2 + 1):
        func_recored[n] += func(i)
    return func_recored[n]

n = int(input())
print(func(n))
