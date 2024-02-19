# 문제
## 나만의 카카오 성격 유형 검사지를 만드려고 한다.

### 1번 지표 : R(라이언형), T(튜브형)
### 2번 지표 : C(콘형), F(프로도형)
### 3번 지표 : J(제이지형), M(무지형)
### 4번 지표 : A(어피치형), N(네오형)


## 검사지에는 총 n개의 질문이 있고, 각 7개의 선택지

# 매우 비동의 : 네오형 3점
# 비동의 : 네오형 2점
# 약간 비동의 : 네오형 1점
# 모르겠음 : x
# 약간 동의 : 어피치형 1점
# 동의 : 어피치형 2점
# 매우 동의 : 어피치형 3점

# 매개변수

## 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와
## 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 주어집니다. 

# 제한사항

## 1 ≤ survey의 길이 ( = n) ≤ 1,000
## survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나입니다.

## choices의 길이 = survey의 길이



# # survey
# ["AN", "CF", "MJ", "RT", "NA"]	
# # choices
# [5, 3, 2, 7, 5]	
# # result
# "TCMA"


def solution(survey, choices):
  dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0} 
  ## R, T 
  ## C, F
  ## J, M
  ## A, N
  for i in range(len(choices)):
    ## 점수 없는 선택
    if choices[i] == 4:
      continue
    elif choices[i] > 4: 
      dict[survey[i][1]] += choices[i] - 4
    elif choices[i] < 4:
      dict[survey[i][0]] += 4 - choices[i]
  answer = ''
  if dict["R"] >= dict["T"]:
    answer += 'R'
  else: 
    answer += 'T'
  if dict['C'] >= dict["F"]:
    answer += 'C'
  else: 
    answer += 'F'
  if dict['J'] >= dict["M"]:
    answer += 'J'
  else: 
    answer += 'M'
  if dict['A'] >= dict["N"]:
    answer += 'A'
  else: 
    answer += 'N'
  return answer

a = solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])

print(a)