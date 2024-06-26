N = int(input())

num_list = list(map(int,input().split()))

left = 0
right = 0
count = [0] * (10)
kind = 0

while right < N:
    if count[num_list[right]] == 0:
        kind += 1
    
    count[num_list[right]] += 1
    if kind > 2:
        count[num_list[left]] -= 1
        if count[num_list[left]] == 0:
            kind -= 1
        left += 1
    right += 1
print(right-left)