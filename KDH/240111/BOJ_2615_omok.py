arr = [list(map(int,input().split()))for _ in range(19)]


def row(x,y):
    global flag
    cnt = 1
    for i in range(1,7):
        if i < 6:
            if x+i < 19:
                if arr[x+i][y] == arr[x][y]:
                    cnt += 1
        if i == 6:
            if cnt == 5:
                if x+i < 19:
                    if arr[x][y] == arr[x+i][y]:
                        return
                else:
                    if x-1 >= 0:
                        if arr[x-1][y] != arr[x][y]:
                            print(arr[x][y])
                            print(x+1, y+1)
                            flag = 1
                            return
                    elif x == 0:
                        print(arr[x][y])
                        print(x+1, y+1)
                        flag = 1
                        return
            else:
                # print(x,y, "row")
                return

def col(x,y):
    global flag
    cnt = 1
    for i in range(1,7):
        if i < 6:
            if y+i < 19:
                if arr[x][y+i] == arr[x][y]:
                    cnt += 1
        if i == 6:
            if cnt == 5:
                if y+i < 19:
                    if arr[x][y] == arr[x][y+i]:
                        return
                else:
                    if y-1 >= 0:
                        if arr[x][y-1] != arr[x][y]:
                            print(arr[x][y])
                            print(x+1, y+1)
                            flag = 1
                            return
                    elif y == 0:
                        print(arr[x][y])
                        print(x+1, y+1)
                        flag = 1
                        return
            else:
                # print(x,y, "col")
                return

def cross(x,y):
    global flag
    cnt = 1
    for i in range(1,7):
        if i < 6:
            if x+i <19 and y+i < 19:
                if arr[x+i][y+i] == arr[x][y]:
                    cnt += 1
        if i == 6:
            if cnt == 5:
                if y+i < 19 and x+i < 19:
                    if arr[x][y] == arr[x+i][y+i]:
                        return
                else:
                    if x-1 >= 0 and y-1 >= 0:
                        if arr[x-1][y-1] != arr[x][y]:
                            print(arr[x][y])
                            print(x+1, y+1)
                            flag = 1
                            return
                    elif x == 0 or y == 0:
                        print(arr[x][y])
                        print(x+1, y+1)
                        flag = 1
                        return
            else:
                # print(x,y, "cross")
                return

def cross2(x,y):
    global flag
    cnt = 1
    for i in range(1,7):
        if i < 6:
            if x-i >= 0 and y+i < 19:
                if arr[x-i][y+i] == arr[x][y]:
                    cnt += 1
        if i == 6:
            if cnt == 5:
                if y+i < 19 and x-i >= 0:
                    if arr[x][y] == arr[x-i][y+i]:
                        return
                else:
                    if x+1 <= 18 and y-1 >= 0:
                        if arr[x+1][y-1] != arr[x][y]:
                            print(arr[x][y])
                            print(x+1, y+1, 'a')
                            flag = 1
                            return
                    elif x == 18 or y == 0:
                        print(arr[x][y])
                        print(x+1, y+1, 'b')
                        flag = 1
                        return
            else:
                # print(x,y, "cross")
                return
                 
flag = 0


for i in range(19):
    for j in range(19):
        if arr[i][j] in [1,2]:
            row(i,j)
            col(i,j)
            cross(i,j)
            cross2(i,j)
if flag == 0:
    print(0)
