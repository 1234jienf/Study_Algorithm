# N = int(input())
# jum_list = []
# for _ in range(N):
#     X,Y = map(int, input().split())
#     jum_list.append((X,Y))



# plus = 0
# minus = 0
# boom = 0
# jum_list.sort()

# first_x = jum_list[0][0]
# first_y = jum_list[0][1]
# last_x = jum_list[-1][0]
# last_y = jum_list[-1][1]

# if first_y > last_y:
#     for i in range(1,N):
#         # x좌표가 시작과 끝점 사이에 있는경우
#         if first_x < jum_list[i][0] < last_x:
#             # y좌표가 둘 사이면
#             if first_y < jum_list[i][1] < last_y:
#                 boom = 1
            
            
#         elif first_y    

# elif first_y < last_y:
#     pass

# # 처음점과 마지막 점의 y좌표가 같을 때
# else:
#     pass

# if boom == 0:
#     ans = last_x - first_x
# else:
#     ans = -1
# print(ans)

#---------------------------------------


from collections import deque

N = int(input())
Jum = deque()
min_X = 9999999999
max_X = -999999999
min_Y = 999999999
max_Y = -99999999999
flag = 1
for i in range(N):
    X,Y = map(int, input().split())
    if X < min_X:
        min_X = X
    elif X > max_X:
        max_X = X
    if Y < min_Y:
        min_Y = Y
    elif Y > max_Y:
        max_Y = Y
    Jum.append((X,Y))
# print(max_X,min_X,max_Y,min_Y)
while Jum:
    now = Jum.popleft()
    if now[0] != min_X and now[0] != max_X:        
        if min_Y < now[1] < max_Y:
            flag = 0
        if max_X - min_X != max_Y - min_Y:
            flag = 0
        else:
            continue
    else:
        continue
    
if flag:
    print(max((max_X-min_X,max_Y-min_Y)))
else:
    print(-1)

# --------------------------------------------




        


