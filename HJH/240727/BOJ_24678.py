import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    for num in tuple(map(int, input().split())):
        if num % 2 == 0:
            cnt += 1
    print('R' if cnt >= 2 else 'B')
# 이런 문제를... 죄송합니다
# 여러번 노트에 적은결과
# 짝 짝 짝
# 짝 짝 홀
# 의 경우 R이 이깁니다.