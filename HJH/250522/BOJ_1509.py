s = input()
size = len(s)
palindrome = [[False] * size for _ in range(size)]

palindrome[0][0] = True
if size >= 2:
    palindrome[1][1] = True
    if s[0] == s[1]:
        palindrome[0][1] = True
if size >= 3:
    palindrome[2][2] = True
    if s[1] == s[2]:
        palindrome[1][2] = True
    if s[0] == s[2]:
        palindrome[0][2] = True

for end in range(3, size):
    palindrome[end][end] = True
    # 1. 길이 2 검사
    if s[end-1] == s[end]:
        palindrome[end-1][end] = True
    # 2. 길이 3 검사
    if s[end-2] == s[end]:
        palindrome[end-2][end] = True
    # 3. 길이 4 이상 검사
    for start in range(end-1, -1, -1):
        if palindrome[start+1][end-1] and s[start] == s[end]:
            palindrome[start][end] = True

dp = [0] * (size+1)
for end in range(size):
    dp[end] = 2501
    for start in range(end+1):
        if palindrome[start][end]:
            dp[end] = min(dp[end], dp[start-1] + 1)
print(dp[size-1])