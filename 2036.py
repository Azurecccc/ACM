def my_search(depth, now_acid, now_bitter, have_take_one):
    if depth == n:
        if have_take_one:
            global ans
            ans = min(ans, abs(now_acid - now_bitter))
        return
    my_search(depth + 1, now_acid, now_bitter, have_take_one=have_take_one)  # 不要第depth个食物
    my_search(depth + 1, now_acid * s[depth], now_bitter + b[depth], have_take_one=True)

n = int(input())
s = []
b = []
for i in range(n):
    a1, a2 = [int(x) for x in input().split()]
    s.append(a1)
    b.append(a2)
ans = abs(s[0] - b[0])
my_search(-1, 1, 0, have_take_one=False)
print(ans)



