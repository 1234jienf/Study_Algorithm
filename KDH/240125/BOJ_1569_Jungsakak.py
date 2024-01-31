N = int(input())
jum_list = []
for _ in range(N):
    X,Y = map(int, input().split())
    jum_list.append((X,Y))



plus = 0
minus = 0
boom = 0
jum_list.sort()

first_x = jum_list[0][0]
first_y = jum_list[0][1]
last_x = jum_list[-1][0]
last_y = jum_list[-1][1]

if first_y > last_y:
    for i in range(1,N):
        # x좌표가 시작과 끝점 사이에 있는경우
        if first_x < jum_list[i][0] < last_x:
            # y좌표가 둘 사이면
            if first_y < jum_list[i][1] < last_y:
                boom = 1
            
            
        elif first_y    

elif first_y < last_y:
    pass

# 처음점과 마지막 점의 y좌표가 같을 때
else:
    pass

if boom == 0:
    ans = last_x - first_x
else:
    ans = -1
print(ans)
        


