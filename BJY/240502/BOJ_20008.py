# 문제
## 가장 빠른 시간 내에 몬스터를 처치하려고 한다. 
## 사용할 수 있는 스킬은 N개 있으며, 각 스킬은 사용하는 데 1초가 들고,
## 사용을 시작한 지 1초 후 몬스터에게 일정 대미지를 입힌다.
## 여러 개의 스킬을 동시에 사용할 수는 없다.

## 각 스킬에는 저마다의 대기 시간과 대미지가 있다. 
## 대기 시간은 스킬을 사용하기 시작한 순간부터 차기 시작한다.
## 예를 들어, 현재 시각이 t = 0이고, 대기 시간이 10초이고
## 대미지가 10인 스킬을 체력이 100인 몬스터에게 사용했다고 하자.
## 그러면 t = 1일 때 몬스터의 체력이 90으로 줄어들고, 같은 스킬은 t = 10일 때부터 다시 사용할 수 있다.


## 입력

# 첫 번째 줄에는 스킬 개수 N(1 ≤ N ≤ 5)과 몬스터의 체력(HP)을 나타내는 정수(1 ≤ HP ≤ 100000)가 주어진다.
# 두 번째 줄부터는 줄마다 스킬의 대기 시간을 초 단위로 나타내는 정수 C(1 ≤ C ≤ 10)와 
# 스킬의 대미지를 나타내는 정수 D(HP/10 ≤ D ≤ HP)가 공백을 두고 주어진다. 
# 든 스킬의 대기 시간은 다르며, 모든 D의 합은 HP보다 작다.


## 출력

# 몬스터를 처치하는 데 걸리는 최소 시간을 출력한다.

from itertools import permutations

t_time=0
t_damage = 0

N, HP = map(int,input().split())
lst = []

for i in range(N):
    C, D = map(int,input().split())
    t_time += C
    t_damage += D
    lst.append((C,D))
    
def damage_lst(t, damage, d_lst):
    global limit
    idx = 0
    while idx < limit:
        if d_lst[idx] != 0:
            idx += 1
            continue
        d_lst[idx] = damage
        idx += t
    return d_lst

def time_cnt(d_lst, hp):
    cnt = 0
    for i in range(len(d_lst)):
        if hp <= 0:
            break
        hp -= d_lst[i]
        cnt += 1
    return cnt

limit = t_time*((HP//t_damage)+1)
lst = list(permutations(lst, N))
# print(lst)
result = 1e10

for i in range(len(lst)):
    d_lst = [0 for _ in range(t_time * ((HP // t_damage)+1))]
    for t, d in lst[i]:
        d_lst = damage_lst(t,d,d_lst)
    result = min(result, time_cnt(d_lst, HP))
    
print(result)

# p_lst = permutations(lst,N)
# print(p_lst)
    

# ans = 0