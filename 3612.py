s, m = input().split()
m = int(m)
n = len(s)


def solve(m, my_pow):
    if my_pow == 0:
        return m
    half = n * (2 ** (my_pow - 1))
    if m <= half:
        return solve(m, my_pow - 1)
    elif m == half + 1:
        return solve(half, my_pow - 1)
    else:
        return solve(m - 1 - half, my_pow - 1)

print(s[solve(m, 70) - 1])
