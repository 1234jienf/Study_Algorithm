import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = 0
for _ in range(n):
    num = int(input())
    if stack and stack[-1] > num:
        ans += len(stack)
        stack.append(num)
    else:
        while stack and stack[-1] <= num:
            stack.pop()
        ans += len(stack)
        stack.append(num)
print(ans)