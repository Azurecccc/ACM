n = int(input())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

a = sorted(a, key=lambda x: x[2])

ans = 0
import math
for i in range(1, n):
    dx = a[i][0] - a[i - 1][0]
    dy = a[i][1] - a[i - 1][1]
    dz = a[i][2] - a[i - 1][2]
    ans += math.sqrt(dx * dx + dy * dy + dz * dz)
print('%.3f'%(ans))
