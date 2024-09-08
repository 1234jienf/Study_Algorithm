# 문제
## 크기가 N인 배열 a가 주어진다. 
## 배열 a의 임의의 위치를 나타내는 두 수 i, j를 골랐을 때, 아래 두 조건을 만족하면 같은 수 순서쌍 (i, j)를 만들 수 있다.

### 1 ≤ i ≤ j ≤ N
### ai = aj

## 만들어진 같은 수 순서쌍 (i, j)의 합은 ai부터 aj까지의 합 ai + ai+1 + ai+2 + … + aj-1 + aj로 정의된다.
## 이때 주어진 배열에서 만들 수 있는 같은 수 순서쌍의 최대 합을 찾고, 최대 합을 가지는 같은 수 순서쌍의 개수를 출력하는 프로그램을 작성하시오.


# 입력
## 첫 번째 배열 a의 크기 N이 주어진다.
## 두 번째 줄에 배열 a의 원소 a1, a2, …, aN이 주어진다.

# 출력
## 주어진 배열에서 만들 수 있는 같은 수 순서쌍의 최대 합과 최대 합을 가진 같은 수 순서쌍의 개수를 출력한다.

N = int(input())

arr = list(map(int,input().split()))

max_sum = 0
max_count = 0
dic = {}
for i in range(N):
  if arr[i] not in dic:
    dic[arr[i]] = []
    if arr[i] > max_sum:
      max_sum = arr[i]
      max_count = 1
    elif arr[i] == max_sum:
      max_count += 1
  dic[arr[i]].append(i)

# 누적 합 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
  prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for num, pos_list in dic.items():
  ## 같은 숫자가 두번 있다면
  if len(pos_list) > 1:
    # current = sum(arr[pos_list[0]:pos_list[-1] + 1])
    # if current > max_sum:
    #   max_sum = current
    #   max_count = 1
    # elif current == max_sum:
    #   max_count += 1
    current = prefix_sum[pos_list[-1]+1] - prefix_sum[pos_list[0]]
    if current > max_sum:
      max_sum = current
      max_count = 1
    elif current == max_sum:
      max_count += 1


print(max_sum,max_count)