import sys
sys.stdin = open('22988.txt', 'r')

# 입력
N, X = map(int, input().split())
array = list(map(int, input().split()))

# 정렬 후 꽉찬 용기 제거후 카운트
array.sort()
count = 0
count += array.count(X)
for i in range(count):
    array.pop()

# 투 포인터
s = 0
e = N - 1 - count
rest_count = N - count
while s < e:
    # 두개 합친거 X/2보다 크면 제거후 카운트
    if array[s] + array[e] >= X / 2:
        count += 1
        rest_count -= 2
        e -= 1
        s += 1
    # 아니면 다음거 보기
    else:
        s += 1

print(count + rest_count // 3)
