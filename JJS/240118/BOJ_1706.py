import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(str, input().strip()))for _ in range(r)]
word = []

# 가로 탐색
for i in range(r):
    width_word = ""
    for j in range(c):
        # #이 아니면 낱말 만들기
        if board[i][j] != "#":
            width_word += board[i][j]
        
        # #을 만났는데 글자가 있다면 추가
        elif len(width_word) >= 2:
                word.append(width_word)

        else:
            width_word = ""

    if len(width_word) >= 2:
        word.append(width_word)

# 세로 탐색
for i in range(c):
    length_word = ""
    for j in range(r):
        if board[j][i] != "#":
            length_word += board[j][i]
        elif len(length_word) >= 2:
            word.append(length_word)
        else:
            length_word = ""

    if len(length_word) >= 2:
        word.append(length_word)

# 모인 단어 알파벳 순으로 정렬
word.sort()
print(word[0])