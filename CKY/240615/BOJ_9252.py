# 재귀 제한 해제
import sys
sys.setrecursionlimit(10000)

# 재귀함수를 통해서 문자 찾기
def backtracking(start, value):
    global max_value
    global ans
    global word_two
    # 최대 길이 도달했을때 종료
    if value == 0:
        print(max_value)
        print(ans[::-1])
        exit()
    # 현재 칸에서 위로 간 값과 왼쪽으로 간 값을 비교해서 작은 값찾는 재귀
    else:
        if matrix[start[0]-1][start[1]] == value:
            backtracking([start[0]-1,start[1]],value)
        elif matrix[start[0]][start[1]-1] == value:
            backtracking([start[0],start[1]-1],value)
        # 만약 왼쪽과 위 둘다 작은 경우 왼쪽위로 인덱스 변경 후 문자 저장
        elif matrix[start[0]-1][start[1]] < value and matrix[start[0]][start[1]-1] < value:
            ans += word_two[start[1]-1]
            backtracking([start[0]-1,start[1]-1],value-1)


word_one = input()
word_two = input()

one_length = len(word_one)
two_length = len(word_two)

matrix = [[0]* (two_length+1) for _ in range(one_length+1)]
max_value = 0
ans = ""
# LCS 구하는 알고리즘
for i in range(one_length+1):
    for j in range(two_length+1):
        if i == 0 or j == 0:
            continue
        else:
            if word_two[j-1] == word_one[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    if matrix[i][j] > max_value:
        max_value = matrix[i][j]
if max_value == 0:
    print(0)
else:
    backtracking([one_length,two_length],max_value)