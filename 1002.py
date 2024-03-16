def check_forbid(x, y):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2, 0]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1, 0]
    for j in range(9):
        if horse_x + dx[j] == x and horse_y + dy[j] == y:
            return False
    return True


B_x, B_y, horse_x, horse_y = [int(x) for x in input().split()]
nums = [[0 for j in range(B_y + 1)] for i in range(B_x + 1)]
for i in range(B_x + 1):
    for j in range(B_y + 1):
        if i == 0 and j == 0:
            nums[i][j] = 1
        else:
            if check_forbid(i, j):
                if i > 0:
                    nums[i][j] += nums[i - 1][j]
                if j > 0:
                    nums[i][j] += nums[i][j - 1]
            else:
                pass
print(nums[B_x][B_y])

