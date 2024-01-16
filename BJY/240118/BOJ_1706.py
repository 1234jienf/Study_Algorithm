# 입력
## 첫째 줄에는 퍼즐의 R과 C가 빈 칸을 사이에 두고 주어진다.
### (2 ≤ R, C ≤ 20) 
## 이어서 R개의 줄에 걸쳐 다 푼 퍼즐이 주어진다. 
## 각 줄은 C개의 알파벳 소문자 또는 금지된 칸을 나타내는 #로 이루어진다.


# 출력
## 첫째 줄에 사전식 순으로 가장 앞서 있는 낱말을 출력한다.

R,C = map(int,input().split())
arr = [list(map(str,input()))for _ in range(R)]

answer = []
## 가로줄 단어 

for i in range(R):
    word = ""
    for j in range(C):
        if arr[i][j] == '#':
            if word and len(word) > 1:
                answer.append(word)
            word == ""
        else:
            word += arr[i][j]
    if word and len(word) > 1:
        answer.append(word)
        
for j in range(C):
    word= ''
    for i in range(R):
        if arr[i][j] == '#':
            if word and len(word) > 1:
                answer.append(word)
            word == ""
        else:
            word += arr[i][j]
    if word and len(word) > 1:
        answer.append(word)
    
answer.sort()
if answer:
    print(answer[0])
else:
    print('')