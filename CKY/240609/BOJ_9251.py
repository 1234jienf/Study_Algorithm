word_one = input()
word_two = input()

# 처음 단어의 길이
one_length = len(word_one)
# 두번째 단어의 길이
two_length = len(word_two)
# LCS 적용할 리스트
LCS_matrix = [ [0]*(one_length+1) for _ in range(two_length+1)]
# 최대값 체크할 변수
max_value = 0
# 처음단어 반복문
for i in range(one_length+1):
    # 두번째 단어 반복문
    for j in range(two_length+1):
        # 0 인덱스는 0 처리
        if i == 0 or j == 0:
            LCS_matrix[j][i] = 0
        else:
            # word_one 과 word_two 가 같은경우
            if word_one[i-1] == word_two[j-1]:
                # LCS_matrix[i-1][j-1] 값 + 1 한 값을 갱신
                LCS_matrix[j][i] = LCS_matrix[j-1][i-1] + 1
            else:
                # 값이 다른경우 i-1 과 j-1 에서 둘중 큰 값을 갱신
                LCS_matrix[j][i] = max(LCS_matrix[j-1][i], LCS_matrix[j][i-1])
    if LCS_matrix[j][i] > max_value:
        max_value = LCS_matrix[j][i]

print(max_value)