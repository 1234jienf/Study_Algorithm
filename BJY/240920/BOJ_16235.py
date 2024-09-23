# 문제
## 부동산 투자로 억대의 돈을 번 상도는 최근 N×N 크기의 땅을 구매했다. 
## 상도는 손쉬운 땅 관리를 위해 땅을 1×1 크기의 칸으로 나누어 놓았다.
## 각각의 칸은 (r, c)로 나타내며, r은 가장 위에서부터 떨어진 칸의 개수, c는 가장 왼쪽으로부터 떨어진 칸의 개수이다. 
## r과 c는 1부터 시작한다.

## 상도는 전자통신공학과 출신답게 땅의 양분을 조사하는 로봇 S2D2를 만들었다. 
## S2D2는 1×1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 모든 칸에 대해서 조사를 한다. 
## 가장 처음에 양분은 모든 칸에 5만큼 들어있다.

## 매일 매일 넓은 땅을 보면서 뿌듯한 하루를 보내고 있던 어느 날 이런 생각이 들었다.

## 나무 재테크를 하자!

## 나무 재테크란 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익을 얻는 재테크이다. 
## 상도는 나무 재테크로 더 큰 돈을 벌기 위해 M개의 나무를 구매해 땅에 심었다.
## 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.

## 이 나무는 사계절을 보내며, 아래와 같은 과정을 반복한다.

## 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
## 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
## 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
## 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

## 여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
## 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 
## 소수점 아래는 버린다.

## 가을에는 나무가 번식한다. 
## 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
## 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
## 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

## 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 
## 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

## K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.

# 입력
## 첫째 줄에 N, M, K가 주어진다.

## 둘째 줄부터 N개의 줄에 A배열의 값이 주어진다.
## r번째 줄의 c번째 값은 A[r][c]이다.

## 다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 
## 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.

# 출력
## 첫째 줄에 K년이 지난 후 살아남은 나무의 수를 출력한다.

# 처음에 양분이 모두 5씩 들어있다.
# 봄 -> 나이만큼 양분을 먹고, 나이 1 증가 (어린 나무 부터 양분 먹기) / 양분 못먹으면 죽음
# 여름 -> 봄에 죽은 나무가 양분으로 변함 int(나이 //2)
# 가을 -> 나무 번식. 조건 : 나이가 5의 배수, 인접한 8 칸(나이가 1)
# 겨울 -> S2D2가 돌아다니며 양분 추가 (arr만큼 주어짐)
dr = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

N, M, K = map(int, input().split())
ground = [[5] * N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
trees = []

for i in range(M):
    x, y, z = map(int, input().split())
    trees.append((x, y, z))

trees.sort(key=lambda x: x[2])  # 나무의 나이를 기준으로 정렬

year = 0

while year < K:
    nut = []  # 죽은 나무 좌표와 나이 저장
    new_tree = []  # 살아남은 나무 저장 리스트

    ## 봄: 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    for i in range(len(trees)):
        x, y, age = trees[i]
        if age <= ground[x - 1][y - 1]:  # 양분이 충분하면
            ground[x - 1][y - 1] -= age  # 나이만큼 양분을 먹고
            new_tree.append((x, y, age + 1))  # 나이가 1 증가
        else:
            nut.append((x, y, age))  # 먹지 못한 나무는 죽음

    ## 여름: 죽은 나무가 양분으로 변환됨
    for x, y, age in nut:
        ground[x - 1][y - 1] += age // 2  # 죽은 나무가 양분으로 변환
    new = []
    ## 가을: 나무 번식
    for i in range(len(new_tree)):
        x, y, age = new_tree[i]
        if age % 5 == 0:  # 나이가 5의 배수인 나무만 번식
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                if 1 <= nx <= N and 1 <= ny <= N:  # 땅을 벗어나지 않는 경우
                    new.append((nx, ny, 1))  # 나이가 1인 나무 번식

    ## 겨울: 양분 추가
    for i in range(N):
        for j in range(N):
            ground[i][j] += arr[i][j]  # 각 칸에 추가된 양분만큼 더해줌

    trees = new + new_tree  # 살아남은 나무와 번식된 나무들로 갱신
    year += 1  # 한 해가 지남

print(len(trees))  # K년 후 살아남은 나무의 개수를 출력


dr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

N, M, K = map(int, input().split())
ground = [[5] * N for _ in range(N)]  # 각 칸의 초기 양분은 5
arr = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 추가될 양분 정보

# 각 칸에 심어진 나무들의 나이를 저장하는 리스트 (2차원 리스트)
trees = [[[] for _ in range(N)] for _ in range(N)]

# M개의 나무 입력 받기
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)  # 나무 심기

# K년 동안 진행
for _ in range(K):
    # 봄과 여름: 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    dead_trees = [[0] * N for _ in range(N)]  # 죽은 나무가 남긴 양분
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                new_trees = []
                trees[i][j].sort()  # 어린 나무부터 처리하기 위해 정렬
                for age in trees[i][j]:
                    if ground[i][j] >= age:
                        ground[i][j] -= age  # 나이만큼 양분을 먹고
                        new_trees.append(age + 1)  # 나이가 1 증가한 나무 저장
                    else:
                        dead_trees[i][j] += age // 2  # 죽은 나무가 양분으로 변환
                trees[i][j] = new_trees  # 살아남은 나무로 갱신

    # 여름: 죽은 나무가 남긴 양분을 땅에 추가
    for i in range(N):
        for j in range(N):
            ground[i][j] += dead_trees[i][j]

    # 가을: 나무 번식
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:  # 나이가 5의 배수인 나무만 번식
                    for dx, dy in dr:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:  # 범위를 벗어나지 않으면
                            trees[ni][nj].append(1)  # 나이가 1인 나무 추가

    # 겨울: 땅에 양분 추가
    for i in range(N):
        for j in range(N):
            ground[i][j] += arr[i][j]  # 각 칸에 양분 추가

# 살아남은 나무의 수 세기
result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])  # 각 칸에 있는 나무의 수를 셈

print(result)
