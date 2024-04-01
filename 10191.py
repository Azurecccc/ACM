
n = int(input())
G = {}
for i in range(n):
    G[i] = []
f = [int(x) for x in input().split()]
for i in range(n - 1):
    G[f[i]].append(i + 1)


def dfs(u):
    global vis
    vis[u] = 1
    for v in G[u]:
        if vis[v] == 0:
            dfs(v)

Q = int(input())
for _ in range(Q):
    a = [int(x) for x in input().split()]
    a = a[1:]
    for i in range(n - 1, -1, -1):
        vis = [0] * n
        dfs(i)
        flag = True
        for o in a:
            if vis[o] == 0:
                flag = False
        if flag:
            print(i)
            break
    
    
