N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))

N_lst.sort()


for num in M_lst:
  ## idx값으로
  left,right = 0, N-1
  found = False
  while left <= right:
    mid = ( left + right )//2
    if N_lst[mid] == num:
      found = True
      break
    else:
      if N_lst[mid] > num:
        right = mid - 1
      else:
        left = mid + 1
  print(1 if found else 0)