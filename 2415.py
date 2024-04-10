a = [int(x) for x in input().split()]
n = len(a)
ans = 0
for x in a:
    ans += x * (2 ** (n - 1))
print(ans)


