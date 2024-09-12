# 문제
## 크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.

### R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
### C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.

## 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다.
## 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 
## 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.

## 예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 
## 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 
## 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.

## 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. 
## R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 
## 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다.
## 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.

## 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.

## 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.

# 입력
## 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)

## 둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 
## 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.

# 출력
## A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 
## 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다.
from collections import Counter

# 입력 받기
r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

# 초기 변수 설정
time = 0
row, col = 3, 3  # 초기 행, 열 크기

# 정렬 후 배열을 갱신하는 함수
def sort_arr():
    global row, col
    if row >= col:  # R 연산
        new_arr = []
        max_len = 0  # 최대 행 길이 계산
        for i in range(row):
            count = Counter([num for num in arr[i] if num != 0])  # 0을 제외한 숫자의 개수 세기
            sorted_row = sorted(count.items(), key=lambda x: (x[1], x[0]))  # 등장 횟수, 숫자 기준으로 정렬
            new_row = []
            for num, cnt in sorted_row:
                new_row.extend([num, cnt])
            max_len = max(max_len, len(new_row))  # 최대 행 길이 갱신
            new_arr.append(new_row)
        # 모든 행의 길이를 최대 길이에 맞춤 (빈 칸은 0으로 채우기)
        for i in range(len(new_arr)):
            new_arr[i].extend([0] * (max_len - len(new_arr[i])))
        arr[:] = new_arr  # 배열 갱신
        col = max_len  # 열 크기 갱신
    else:  # C 연산
        new_arr = []
        max_len = 0  # 최대 열 길이 계산
        for j in range(col):
            column = [arr[i][j] for i in range(row) if arr[i][j] != 0]  # 0을 제외한 숫자만 추출
            count = Counter(column)  # 숫자의 개수 세기
            sorted_col = sorted(count.items(), key=lambda x: (x[1], x[0]))  # 등장 횟수, 숫자 기준으로 정렬
            new_col = []
            for num, cnt in sorted_col:
                new_col.extend([num, cnt])
            max_len = max(max_len, len(new_col))  # 최대 열 길이 갱신
            new_arr.append(new_col)
        # 모든 열의 길이를 최대 길이에 맞춤 (빈 칸은 0으로 채우기)
        max_len = max([len(new_arr[i]) for i in range(len(new_arr))])
        transposed_arr = [[0] * max_len for _ in range(col)]  # 새로운 배열 생성
        for j in range(col):
            for i in range(len(new_arr[j])):
                transposed_arr[j][i] = new_arr[j][i]
        arr[:] = list(map(list, zip(*transposed_arr)))  # 전치해서 배열 갱신
        row = max_len  # 행 크기 갱신

# 반복 수행
while time <= 100:
    if r <= row and c <= col and arr[r-1][c-1] == k:  # 원하는 값이 위치에 있을 때
        print(time)
        break
    sort_arr()  # R 연산 또는 C 연산 수행
    time += 1

if time > 100:
    print(-1)
