def func(a, b):
    mn = min(a, b)
    mx = max(a, b)
    if mn == 0:
        return 0
    return 4 * mn * (mx // mn) + func(mn, mx % mn)

a, b = [int(x) for x in input().split()]
print(func(a, b))

