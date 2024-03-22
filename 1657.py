def dfs(ith_people, have_choose):
    if ith_people == n:
        global  ans
        ans += 1
        return
    for book in like_books[ith_people]:
        if not have_choose[book]:
            have_choose[book] = True
            dfs(ith_people + 1, have_choose)
            have_choose[book] = False

ans = 0
n = int(input())
like_books = [[] for i in range(n)]
have_choose = [0] * (n + 1)
for i in range(n):
    a, b = [int(x) for x in input().split()]
    like_books[i].append(a)
    like_books[i].append(b)
dfs(0, have_choose)
print(ans)
