import sys
def func(s):
    n = len(s)
    if n == 1:
        return 1
    first_half = s[:n//2]
    second_half = s[-1:n//2-1:-1]
    if first_half == second_half:
        return func(s[:n//2])
    else:
        return n


s = input()
print(func(s))
