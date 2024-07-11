N = int(input())
K = int(input())
num_list = list(map(int,input().split()))

if K >= N:
    print(0)
else:
    cnt = 0
    num_list.sort()
    answer_list = []
    for i in range(1,N):
        if num_list[i] != num_list[i-1]:
            answer_list.append(num_list[i]-num_list[i-1])
        else:
            cnt += 1
    answer_list.sort()
    print(sum(answer_list[:N-cnt-K]))