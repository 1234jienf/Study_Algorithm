# 문제
## 틱택토 게임은 두 명의 사람이 번갈아가며 말을 놓는 게임이다.
##  게임판은 3×3 격자판이며, 처음에는 비어 있다.
### 두 사람은 각각 X 또는 O 말을 번갈아가며 놓는데, 
### 반드시 첫 번째 사람이 X를 놓고 두 번째 사람이 O를 놓는다.
### 어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다. 
### 게임판이 가득 차도 게임은 끝난다.
### 게임판의 상태가 주어지면, 그 상태가 틱택토 게임에서 발생할 수 있는 최종 상태인지를 판별하시오


## 입력

# 각 줄은 9개의 문자를 포함하며, 'X', 'O', '.' 중 하나이다. 
# '.'은 빈칸을 의미하며,
# 9개의 문자는 게임판에서 제일 윗 줄 왼쪽부터의 순서이다. 
# 입력의 마지막에는 문자열 "end"가 주어진다.

## 출력

## 각 테스트 케이스마다 한 줄에 정답을 출력한다
## 가능할 경우 "valid", 불가능할 경우 "invalid"를 출력한다.


## 첫번째 풀이 - 그냥 일차원 배열에서 경우 다 때려박아서 하기 -> 예외가 너무 많음..


# def is_winner(X,O,lst):
#     O_win = 0
#     X_win = 0
#     # 가로
#     for i in range(3):
#         if lst[i*3] == lst[i*3+1] == lst[i*3+2]:
#             ## 승리자가 O일 때
#             if lst[i*3] == 'O':
#                 O_win += 1
#             elif lst[i*3] == 'X':
#                 X_win += 1    
#     if O_win != 0 or X_win != 0:
#         if X_win + O_win == 1:
#             print('valid')
#             return
#         else:
#             print('invalid')
#             return
#     else:
#         # 세로
#         for i in range(3):
#             if lst[i] == lst[i+3] == lst[i+6]:
#                 if lst[i] == 'O':
#                     O_win += 1
#                 elif lst[i] == 'X':
#                     X_win += 1 
#         if O_win != 0 or X_win != 0:
#             if X_win + O_win == 1:
#                 print('valid')
#                 return
#             else:
#                 print('invalid')
#                 return
#         else:
#             # 대각선
#             for i in range(1,3):
#                 if lst[4] == lst[4-2*i] == lst[4+2*i]:
#                     if lst[i] == 'O':
#                         O_win += 1
#                     elif lst[i] == 'X':
#                         X_win += 1
#             if O_win != 0 or X_win != 0:
#                 if X_win + O_win == 1:
#                     print('valid')
#                     return
#                 else:
#                     print('invalid')
#                     return
#     ## 9개 -> 아무 조건에도 걸리지 않으면, valid
#     ## 9개 이하인데, 아무 조건에도 걸리지 않으면, invalid
#     if X+O == 9:
#         print('vaild')
#         return
#     else:
#         print('invalid')
#         return

## 두번째 풀이 -> 2차원 배열안에서 정돈 해서, check 함수 돌기 전에 경우 처리 해준 후, 최종 상태인지 아닌지 검증하기
def check(arr,winner):
    # 가료 비교
    if arr[0][0]==arr[0][1]==arr[0][2]==winner:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==winner:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==winner:
        return True
    # 세로 비교
    if arr[0][0]==arr[1][0]==arr[2][0]==winner:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==winner:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==winner:
        return True
    # 대각선 비교
    if arr[0][0]==arr[1][1]==arr[2][2]==winner:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==winner:
        return True
    return False
    



while True:
    lst = list(map(str,input()))
    if len(lst) == 3:
        break
    
    X_num = 0
    O_num = 0
    idx = 0
    arr=[[0]*3 for _ in range(3)]
    for i in range(3):
         for j in range(3):
            arr[i][j]=lst[idx]
            if lst[idx]=="X":
                X_num+=1
            if lst[idx]=="O":
                O_num+=1
            idx+=1
    ### 개수 체크
    if X_num > O_num+1:
        print('invalid')
        continue
    if O_num > X_num:
        print('invalid')
        continue
    if O_num == X_num:
        if check(arr,"O") and not check(arr,"X"):
            print("valid")
            continue
    if O_num + 1 == X_num:
        if check(arr,"X") and not check(arr,"O"):
            print("valid")
            continue
    if X_num == 5 and O_num == 4:
        if not check(arr,"O"):
            print("valid")
            continue
    print("invalid")