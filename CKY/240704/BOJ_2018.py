N = int(input())
# 왼쪽값
left = 1
total = 0
cnt = 1
for i in range(1,N):
    total += i
    # total 값이 N보다 큰경우
    if total > N:
        # N보다 작을때까지 left 빼줌
        while total > N:
            total -= left
            # left 값은 1씩 증가
            left += 1
    # N과 같을경우 cnt 증가 후 left 값을 빼주고 left 증가
    elif total == N:
        cnt += 1
        total -= left
        left += 1
    # 위 연산이 끝났을경우도 cnt 체크
    if total == N:
        cnt += 1

print(cnt)