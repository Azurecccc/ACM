import sys
 
# # 打开文件以供读取
# with open('in.txt', 'r') as file:
#     sys.stdin = file


def bfs(i, j):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = []
    q_head = 0
    q.append((i, j))
    vis[i][j] =  1
    mn_x = mx_x = i
    mn_y = mx_y = j
    tot = 0
    while q_head < len(q):
        x, y = q[q_head]
        mn_x = min(mn_x, x)
        mx_x = max(mx_x, x)
        mn_y = min(mn_y, y)
        mx_y = max(mx_y, y)
        tot += 1
        q_head += 1
        for d in range(4):
            xx = x + dx[d]
            yy = y + dy[d]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            if vis[xx][yy] == 1 or mat[xx][yy] == '.':
                continue
            q.append((xx, yy))
            vis[xx][yy] = 1
    if tot == (mx_x - mn_x + 1) * (mx_y - mn_y + 1):
        return True
    else:
        return False
    

    

n, m = [int(x) for x in input().split()]
mat = []
for i in range(n):
    mat.append(input())
vis = [[0 for j in range(m)] for i in range(n)]
ans = 0
flag = True
for i in range(n):
    for j in range(m):
        if mat[i][j] == '#' and vis[i][j] == 0:
            if not bfs(i, j):
                flag = False
            ans += 1
if flag:
    print(f'There are {ans} ships.')
else:
    print('Bad placement.')
