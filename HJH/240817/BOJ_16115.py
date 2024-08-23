import math

n = int(input())
length = -1
angles = []

# 12시 방향으로부터의 각도를 구한다
def getAngle(y: int, x: int):
    return math.degrees(math.atan2(y, x))

for _ in range(n):
    x, y = map(int, input().split())
    tmpLen = y * y + x * x
    if tmpLen > length:
        length = tmpLen
        angles = [getAngle(y, x)]
    elif tmpLen == length:
        angles.append(getAngle(y, x))

angles.sort()
# 사잇각들을 구한다
anglesEach = [
    angles[i] - angles[i-1] 
    if angles[i] - angles[i-1] > 0 
    else angles[i] - angles[i-1] + 360
    for i in range(len(angles))
]

print(max(anglesEach))