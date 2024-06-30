# 많은 인풋 처리
import sys

input = sys.stdin.readline

N, d, k, c = map(int,input().split())
# 초밥 저장할 리스트
select_list = []

for _ in range(N):
    select_list.append(int(input()))
# 리스트를 k 만큼 확장
for i in range(k-1):
    select_list.append(select_list[i])
# 최대 길이 측정
max_value = 0
# N 까지 반복
for i in range(N):
    # set으로 중복되는 초밥 개수 제거
    sushi_list = set(select_list[i:i+k])
    # 쿠폰이 초밥 리스트 안에 있는 경우 길이 + 1
    if c not in sushi_list:
        count = len(sushi_list) + 1
    # 없으면 길이 count 에 저장
    else:
        count = len(sushi_list)
    # 최대 값이랑 count 비교
    if max_value < count:
        max_value = count

print(max_value)