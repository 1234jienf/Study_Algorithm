import sys

input = sys.stdin.readline

R, C = map(int,input().split())

count = 0

words = [ list(map(str,input().strip())) for _ in range(R) ]

new_words = []

for j in range(C):
    ans = ""
    for i in range(R-1,-1,-1):
        ans += words[i][j]
    new_words.append(ans)

new_words.sort()
max_index = 0

for i in range(1,C):
    index = 0
    if new_words[i-1][index] == new_words[i][index]:
        while new_words[i-1][index] == new_words[i][index]:
            index += 1
        if max_index < index:
            max_index = index
            
print(R - max_index - 1)