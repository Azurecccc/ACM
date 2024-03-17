
def my_search(x, y, vis_book:set, forbidens):
    if x == fx and y == fy:
        global ans
        ans += 1
        return
    vis_book.add((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if new_x < 1 or new_x > n or new_y <1 or new_y > m:
            continue
        if (new_x, new_y) in vis_book:
            continue
        if (new_x, new_y) in forbidens:
            continue
        my_search(new_x, new_y, vis_book, forbidens)
        # 进一层搜索
    vis_book.remove((x, y))


ans = 0
n, m, T = [int(x) for x in input().split()]
sx, sy, fx, fy = [int(x) for x in input().split()]
forbidens = set()
vis_book = set()
for i in range(T):
    x, y = [int(x) for x in input().split()]
    forbidens.add((x, y))
my_search(sx, sy, vis_book, forbidens)
print(ans)
