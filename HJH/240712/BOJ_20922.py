n, k = map(int, input().split())
arr = list(map(int, input().split()))

counter = [0] * 100001
l = 0
r = 1
counter[arr[0]] += 1

ans = 1
while r < n:
    # 지금 r 의 숫자를 더한다
    counter[arr[r]] += 1
    
    # 사이즈가 넘으면 사이즈가 맞을때까지 l을 오른쪽으로 옮긴다.
    while counter[arr[r]] > k:
        counter[arr[l]] -= 1
        l += 1

    r += 1
    
    ans = r - l if r - l > ans else ans

print(ans)