s1, s2, s3, s4 = [int(x) for x in input().split()]
ans = 0
now_mn = 0


def dfs(ith, n, o1, o2):
    if ith == n:
        global now_mn
        now_mn = min(now_mn, max(o1, o2))
        return 
    dfs(ith + 1, n, o1 + times[ith], o2)
    dfs(ith + 1, n, o1, o2 + times[ith])


for _ in range(4):
    times = [int(x) for x in input().split()]
    now_mn = sum(times)
    dfs(0, len(times), 0, 0)
    ans += now_mn
print(ans)
