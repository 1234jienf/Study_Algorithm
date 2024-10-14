# 문제
## 민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 
## 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

## 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

## 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

# 입력
## 첫째 줄에 테스트 케이스의 개수가 주어진다. 
## 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 
## 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 
## 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

# 출력
## 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

tc = int(input())

## 루트 찾기
def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent,size,x,y):
  root_x = find(parent, x)
  root_y = find(parent, y)

  if root_x != root_y:
    if size[root_x] < size[root_y]:
      ## root_y의 사이즈가 더 크다면 큰쪽을 루트로 
      parent[root_x] = root_y
      size[root_y] += size[root_x]
      return size[root_y]
    else:
      parent[root_y] = root_x
      size[root_x] += size[root_y]
      return size[root_x]
  else:
    return size[root_x]  # 같은 집합일 때도 크기를 반환

for i in range(tc):
  ## 친구 F명 <= 100,000
  F = int(input())
  friend_map = {}
  idx = 0
  parent = {}
  size = {}
  for i in range(F):
    a,b = map(str,input().split())
    if a not in friend_map:
      friend_map[a] = idx
      parent[idx] = idx
      size[idx] = 1
      idx += 1
    if b not in friend_map:
      friend_map[b] = idx
      parent[idx] = idx
      size[idx] = 1
      idx += 1
    
    result = union(parent,size,friend_map[a], friend_map[b])
    print(result)
      