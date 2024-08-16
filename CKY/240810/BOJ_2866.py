import sys

input = sys.stdin.readline
# 행, 열 길이
R, C = map(int,input().split())
# 문자열 받아옴
words = [ list(map(str,input().strip())) for _ in range(R) ]
# 문자 역순으로 저장
new_words = []
# 아래서부터 문자열을 저장
for j in range(C):
    ans = ""
    for i in range(R-1,-1,-1):
        ans += words[i][j]
    new_words.append(ans)
# 문자열 정렬
new_words.sort()
# 최종 최대 공통되는 부분 길이 체크
max_index = 0
# 행 길이 만큼 반복
for i in range(1,C):
    # 초기 인덱스값 설정
    index = 0
    # 0번 인덱스부터 앞뒤 비교해가며 값이 같은경우
    if new_words[i-1][index] == new_words[i][index]:
        # 어디까지 공통된 부분인지 체크하는 while 선언
        while new_words[i-1][index] == new_words[i][index]:
            # index 값 1 씩 증가
            index += 1
        # 최고 index 값 갱신
        if max_index < index:
            max_index = index
# 아래서부터 max_index 값을 찾았기 때문에 열의 길이에서 max_index 값에 인덱스 값계산을 한 1을 더해서 정답 출력
print(R - max_index - 1)