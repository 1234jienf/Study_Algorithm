# 문제
## 두 사람이 선물을 주고받은 기록이 있다면,
## 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.

### 예를 들어 A가 B에게 선물을 5번 줬고, B가 A에게 선물을 3번 줬다면 다음 달엔 A가 B에게 선물을 하나 받습니다.

## 두 사람이 선물을 주고받은 기록이 
## 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.

## 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.

### A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7입니다.
### B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1입니다.

## 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶다

# 매개변수
### 친구들의 이름을 담은 1차원 문자열 배열 friends 
### 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 주어짐

# 출력
### 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수

# 제한 사항

## 2 ≤ friends의 길이 = 친구들의 수 ≤ 50
### friends의 원소는 친구의 이름을 의미하는 알파벳 소문자로 이루어진 길이가 10 이하인 문자열입니다.
### 이름이 같은 친구는 없습니다.

## 1 ≤ gifts의 길이 ≤ 10,000
### gifts의 원소는 "A B"형태의 문자열입니다.
### A는 선물을 준 친구의 이름을 B는 선물을 받은 친구의 이름을 의미하며 공백 하나로 구분됩니다.
from itertools import combinations

def solution(friends, gifts):
    dictionary = {f: i for i, f in enumerate(friends)}
    arr = [[0]* len(friends) for _ in range(len(friends))]
    answerlist = [0] * len(friends)
    present = [[0] * 2 for _ in range(len(friends))]
    answer = 0
    combi = list(combinations(friends,2))
    for gift in gifts:
        give, take = gift.split()
        ## 주고 받은 선물 개수 카운팅
        arr[dictionary[give]][dictionary[take]] += 1
        ## 선물지수 계산
        present[dictionary[give]][0] += 1
        present[dictionary[take]][1] += 1
    
    ## 조합을 통해서 선물 주고 받은 사람 체크
    ## (muzi,ryan)
    for com in combi:
        ## arr[0][1] 과 arr[1][0] 비교
        if arr[dictionary[com[0]]][dictionary[com[1]]] > arr[dictionary[com[1]]][dictionary[com[0]]]:
            answerlist[dictionary[com[0]]] += 1
        elif arr[dictionary[com[0]]][dictionary[com[1]]] < arr[dictionary[com[1]]][dictionary[com[0]]]:
            answerlist[dictionary[com[1]]] += 1
        ## 둘이 주고받은 선물개수가 같을때
        else:
            if present[dictionary[com[0]]][0] - present[dictionary[com[0]]][1] >present[dictionary[com[1]]][0] - present[dictionary[com[1]]][1]:
                answerlist[dictionary[com[0]]] += 1
            elif present[dictionary[com[0]]][0] - present[dictionary[com[0]]][1] < present[dictionary[com[1]]][0] - present[dictionary[com[1]]][1]:
                answerlist[dictionary[com[1]]] += 1
            else:
                continue
                
    return max(answerlist)
#1. TC
# friends = ["muzi", "ryan", "frodo", "neo"]
# gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

# #2. TC
# friends = ["joy", "brad", "alessandro", "conan", "david"]
# gifts =["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

# #3. TC
# friends = ["a", "b", "c"]	
# gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]	

