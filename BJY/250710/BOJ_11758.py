## p1, p2, p3
# (-10,000 ≤ x1, y1, x2, y2, x3, y3 ≤ 10,000) 모든 좌표는 정수
## 세 좌표는 서로 다르다

# 출력 -> 반시계면 1. 시계면 -1. 일직선이면 0

def cross(x,y):
  # 외적 함수
  ## z 스칼라 값의 양수/음수 판별
  ## 선분 a,b -> axb
  ## 오른손 법칙..
  res = x[0]*y[1] - x[1]*y[0]
  if res < 0:
    return -1
  elif res > 0 :
    return 1
  else:
    return 0
  
p = []
for i in range(3):  
  x,y = map(int,input().split())
  p.append((x,y))

## vec2 a -> p2-p1 b -> p3-p2
a = (p[1][0] - p[0][0], p[1][1] - p[0][1])
b = (p[2][0] - p[1][0], p[2][1] - p[1][1])

print(cross(a,b))