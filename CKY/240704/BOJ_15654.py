def backtracking(start):
    global M
    global N
    if start == M:
        print(*ans)
    
    for i in range(N):
        if num_dict[num_list[i]] != 0:
            ans.append(num_list[i])
            num_dict[num_list[i]] -= 1
            backtracking(start+1)
            num_dict[num_list[i]] += 1
            ans.pop()

N,M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
num_dict = {}
for i in num_list:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1
ans = []

backtracking(0)