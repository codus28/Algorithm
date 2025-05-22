
'''
DFS - Backtracking with recursive function
'''
N = int(input())
num = list(map(int, input().split()))
operators = list(map(int,input().split()))

mn = 1e9
mx = -1e9

def dfs(n, tmp):
    global mx, mn

    if n == N-1:
        mx = max(tmp, mx)
        mn = min(tmp, mn)
        return

    if operators[0] != 0:  # 덧셈하는 경우
        operators[0] -= 1
        dfs(n + 1, tmp + num[n + 1])
        operators[0] += 1

    if operators[1] != 0:  # 뺄셈하는 경우
        operators[1] -= 1
        dfs(n + 1, tmp - num[n + 1])
        operators[1] += 1

    if operators[2] != 0:  # 곱셈하는 경우
        operators[2] -= 1
        dfs(n + 1, tmp * num[n + 1])
        operators[2] += 1

    if operators[3] != 0:  # 나눗셈하는 경우
        operators[3] -= 1
        dfs(n + 1, int(tmp / num[n + 1]))
        operators[3] += 1

dfs(0, num[0])
print(mx)
print(mn)

