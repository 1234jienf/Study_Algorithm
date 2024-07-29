"""
합이 0에 가까운 세 용액을 찾는 문제로, 정렬 후 투포인터를 이용하여 구하는 문제이다.
투포인터를 이용하여 양쪽의 값을 더한 후,
음수라면 오른쪽의 수를 하나 더 더하고, 양수라면 왼쪽의 수를 하나 더 더한다.
해당 수를 이전 답과 비교하여 min 값을 구한 뒤,
여전히 양수가 라면 오른쪽 포인터를 한칸 왼쪽으로 하고, 음수라면 왼쪽의 포인터를 한칸 오른쪽으로 한다.
왼쪽 포인터가 양수가 되거나, 오른쪽 포인터가 음수가 될 때 까지 진행한다.

=> 풀이가 이상했고... 다시 해볼것

전체 중 i번째 용액을 선택하고,
i + 1부터 n - 1 번쨰 까지 용액 중 i 번 쨰 용액을 포함한 합이 최소가 되는 값을 갱신해준다.
이 때 투 포인터를 이용하여 탐색하되, 양쪽 점을 나머지 두 용액으로 계산한다.

3개 용액 중 1개를 고정하고, 나머지를 투포인터로 탐색하는 방식

=> 완전탐색이랑 다를게 없는데..?
=> 완전탐색은 N*(N-1)*(N-2) == N^3
=> 이건 (N-2)*(N-1) == N^2
=> 다르네
"""
import sys
sys.stdin = open("./2473.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
arr.sort() # 합이 최소가 되야하니까 정렬해서 큰거 작은거 구분

min_sum = 3000000001
ans = [arr[0], arr[1], arr[N-1]] # 기본 조건 => 안해도 됨

for i in range(N - 2): # 하나를 i 로 고정
    s, e = i + 1, N - 1

    while s < e:
        now = arr[i] + arr[s] + arr[e]

        if abs(now) < abs(min_sum): # 투포인터로 i + 1 부터 N - 1 까지 탐색
            ans = [arr[i], arr[s], arr[e]]
            min_sum = now

        if now < 0:
            s += 1
        elif now > 0:
            e -= 1
        else:
            print(*ans)  # 0이 나오면 출력하고 끝
            exit()

print(*ans) # 0이 없으면 끝까지 탐색

# 질문? 이번주는 투포인터만 두개 ^^7

"""
left, right = 0, N - 1
small = float("inf")
s_left, s_right = 0, N - 1

while arr[left] <= 0 <= arr[right] and (right - left >= 2):
    now = arr[left] + arr[right]
    n_left = arr[left + 1]
    n_right = arr[right - 1]

    if now > 0:
        now += n_left
    elif now < 0:
        now += n_right
    else:
        now = min(abs(n_right), abs(n_left))

    if small > abs(now):
        small = abs(now)
        s_left, s_right = left, right

    if now > 0:
        right -= 1
    elif now < 0:
        left += 1
    else:
        break

ans1 = abs(arr[s_left] + arr[s_right] + arr[s_left + 1])
ans2 = abs(arr[s_left] + arr[s_right] + arr[s_right - 1])

if ans1 < ans2:
    print(arr[s_left], arr[s_left + 1], arr[s_right])
else:
    print(arr[s_left], arr[s_right - 1], arr[s_right])
"""
