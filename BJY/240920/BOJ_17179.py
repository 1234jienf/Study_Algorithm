# 문제
## 생일을 맞이한 주성이가 생일 파티를 준비하려고 한다. 
## 주성이는 일반 케이크 대신 평소 좋아하던 롤 케이크를 준비했다. 
## 롤 케이크에는 장식이 존재해서 특정 위치에서만 자를 수 있다. 
## 주성이는 롤 케이크 조각을 파티에 올 친구의 수 만큼 준비하고 싶어서, 가장 작은 조각의 크기를 미리 알아보기로 했다. \
## 하지만 짓궂은 주성이의 친구들은 생일파티에 몇 명이 참석하는지 직접적으로 알려주지를 않는다. 
## 그래서 몇 개의 수를 목록에 적어, 각 수만큼 조각을 만들었을 때 가장 작은 조각의 길이의 최댓값을 구하려고 한다.

## 예를 들어 70cm의 롤 케이크에 자를 수 있는 지점이 5군데(10cm, 20cm, 35cm, 55cm, 60cm)가 있다고 하자. 
## 만약 목록에 적힌 수 중 하나가 3이라면 이때 가장 작은 조각의 길이는 최대 15cm이다. 
## 예를 들어 20cm, 35cm, 55cm 지점을 자를 때 최대가 된다.

# 입력
## 첫 번째 줄에 자르는 횟수가 담긴 목록의 길이 N과 자를 수 있는 지점의 개수 M, 
## 그리고 롤 케이크의 길이인 정수 L이 주어진다. (1 ≤ N ≤ M ≤ 1,000, 1 < L ≤ 4,000,000)

## 다음 M줄에 걸쳐 자를 수 있는 지점을 나타내는 정수 Si가 주어진다. (1 ≤ Si < L)

## 다음 N줄에 걸쳐 자르는 횟수를 나타내는 정수 Qi가 주어진다. (1 ≤ Qi ≤ M)

## Si는 오름차순으로 주어지고 중복되는 수는 없으며, Qi도 마찬가지이다.

# 출력
## N개 줄에 걸쳐 각 목록에 있는 횟수대로 롤 케이크를 잘랐을 때 가장 작은 조각의 길이의 최댓값을 출력한다.
N, M, L = map(int,input().split())
spots = [int(input()) for _ in range(M)]
tc = [int(input()) for _ in range(N)]

spots.insert(0,0)
spots.append(L)

def cake_cut(mid):
  cnt = 0
  last_cut = 0
  for spot in spots:
    if spot - last_cut >= mid:
      cnt += 1
      last_cut = spot
  return cnt

for case in tc:
  left = 1
  right = L
  ans = 0

  while left <= right:
    mid = (left + right) // 2
    cnt = cake_cut(mid)

    if cnt > case:
      left = mid + 1
      ans = max(ans,mid)
    else:
      right = mid - 1
  print(ans)