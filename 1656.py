def dfs(u):
    global vis
    vis[u] = 1
    global G
    for v in G[u]:
        if vis[v] == 0:
            dfs(v) 


n, m = [int(x) for x in input().split()]


book = []
for i in range(m):
    book.append([int(x) for x in input().split()])
    if book[i][0] > book[i][1]:
        book[i][0], book[i][1] = book[i][1], book[i][0]

ans = []
for i in range(m):
    G = {}
    for j in range(n + 1):
        G[j] = []
    for j in range(m):
        if j != i:
            u, v = book[j]
            G[u].append(v)
            G[v].append(u)
    vis = [0] * (n + 1)
    dfs(1)
    if sum(vis) != n:
        ans.append((book[i][0], book[i][1]))
ans = sorted(ans)
for o in ans:
    print(f'{o[0]} {o[1]}')
