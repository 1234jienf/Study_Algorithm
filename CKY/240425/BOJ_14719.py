H,W = map(int,input().split())

block_list = list(map(int,input().split()))

matrix = [ [0] * W for _ in range(H) ]

rain = 0

for index, block in enumerate(block_list):
    for i in range(block):
        matrix[i][index] = 1

for i in range(H):
    isOpen = False
    check = 0
    for j in range(W):
        if matrix[i][j] == 1:
            if isOpen:
                rain += check
                check = 0
                isOpen = False
            else:
                check = 0
                isOpen = True
        else:
            check += 1
    print(rain)
print(matrix)
print(rain)