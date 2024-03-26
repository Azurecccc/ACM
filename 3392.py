
n, m = [int(x) for x in input().split()]
row_num = {'W':[0] * n, 'B':[0] * n, 'R':[0] * n}

mat = []
for i in range(n):
    mat.append(input())
    for j in range(m):
        row_num[mat[i][j]][i] += 1


def cal(row_up, row_down, c):
    tot  = 0
    for i in range(row_up, row_down):
        tot += (m - row_num[c][i])
    return tot

ans = n * m 
for w in range(n):
    for b in range(w + 1, n):
        for r in range(b + 1, n):
            ans = min(ans, cal(0, w + 1, 'W') + cal(w + 1, b + 1, 'B') + cal(b + 1, n, 'R'))
print(ans)
