# 문제
## 비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열을 찾으려고 합니다.


# 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
# 부분 수열의 합은 k입니다.
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.


## 수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때,
## 위 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는
## solution 함수를 완성해주세요.
## 이때 수열의 인덱스는 0부터 시작합니다.


# 제한사항

## 5 ≤ sequence의 길이 ≤ 1,000,000
### 1 ≤ sequence의 원소 ≤ 1,000
### sequence는 비내림차순으로 정렬되어 있습니다.
## 5 ≤ k ≤ 1,000,000,000
### k는 항상 sequence의 부분 수열로 만들 수 있는 값입니다.




## 입출력 예
## sequence	k	result
# [1, 2, 3, 4, 5]	7	[2, 3]
# [1, 1, 1, 2, 3, 4, 5]	5	[6, 6]
# [2, 2, 2, 2, 2]	6	[0, 2]



def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    answer = [-1, -1]
    
    while right < n:
        if current_sum == k:
            if right - left < min_length:
                min_length = right - left
                answer = [left, right]
            elif right - left == min_length and left < answer[0]:
                answer = [left, right]
                
            current_sum -= sequence[left]
            left += 1
        
        elif current_sum < k:
            right += 1
            if right < n:
                current_sum += sequence[right]
        
        else:
            current_sum -= sequence[left]
            left += 1
    
    return answer

# def calc(idx, n, cnt, sequence, k):
#     while idx + cnt < len(sequence):
#         if n == k:
#             return idx + cnt
#         elif n > k:
#             return 0
#         cnt += 1
#         n += sequence[idx + cnt]
#     return 0


# def solution(sequence, k):
#   # end = len(sequence)
#   # calc(0,sequence[0],[0])
#   answer = []

#   for i in range(len(sequence)):
#     start = sequence[i]
#     if start > k:
#       break
#     else:
#       ans = calc(i, start, 0, sequence, k)
#       if ans != 0:
#         answer.append([i, ans])
  
#   answer.sort(key=lambda x: (x[1] - x[0], x[0]))

#   return answer[0]