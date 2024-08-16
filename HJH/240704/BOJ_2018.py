n = int(input())
least = 0
ans = 0
i = 0

while True:
    i += 1
    # i 개의 연속된 수로 가능한지 검사
    least += i
    if n < least:
        break
    if (n - least) % i == 0:
        ans += 1

print(ans)