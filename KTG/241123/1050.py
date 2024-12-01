"""
같은 재료가 여러번 나올 수 있고, 한 포션을 만드는 레시피가 여러개 일 수 있음
따라서 주어진 레시피를 분해하고 다시 작성하는 과정이 필요함.
"""
import sys
from collections import defaultdict, deque
sys.stdin = open('1050.txt', 'r')

# 시장에서 파는 재료 갯수 N, 물약 식의 갯수 M
N, M = map(int, sys.stdin.readline().rstrip().split())
# 1. 재료 정리
ing_dict = {'-1': True}                          # 재료 사전. {재료 이름: 코스트}
ing_cost = [float('inf') for _ in range(200)]    # 재료 가격 리스트. 각 재료의 가격 (N <= 50 + M <=50 + alpha)
for k in range(N):
    # 이름과 가격 split
    name, cost = input().split()
    # 이름은 사전에, 가격은 리스트에 정리
    ing_dict[name] = k + 1
    ing_cost[k + 1] = int(cost)
# 2. 레시피 정리
recipe_list = [input() for _ in range(M)]
graph = defaultdict(list)                   # 포션 사전 (재료별 포션과 포션 레시피 번호)
recipe_cnt = defaultdict(int)               # 같은 포션 레시피 갯수
recipe_dict = defaultdict(list)             # 포션별 재료 갯수
recipe_order = defaultdict(list)            # 포션별 재료 종류
recipe_list.sort()
for recipe in recipe_list:
    # 2-1. 포션과 각 재료 split
    potion, ingredients = recipe.split('=')
    ing_list = ingredients.split('+')
    # 2-2. 포션도 재료 사전에 정리 및 인덱스 추출
    if ing_dict.get(potion):
        potion_idx = ing_dict[potion]
    else:
        potion_idx = len(ing_dict.keys())
        ing_dict[potion] = potion_idx
    # 2-3. 같은 포션의 인덱스와 레시피 번호를 idx에 저장 => 나중에 재료별로 graph에 저장할 것
    recipe_idx = (potion_idx, recipe_cnt[potion_idx])
    recipe_cnt[potion_idx] += 1
    # 2-4. 레시피의 재료 정리
    temp_set = set()
    temp = defaultdict(int)
    for ingredient in ing_list:
        # 2-4-1. 갯수와 이름 분리
        cnt, name = int(ingredient[0]), ingredient[1:]  # 0 <= cnt <= 9
        # 2-4-2. 재료 사전에 정리 및 인덱스 추출
        if ing_dict.get(name):
            name_idx = ing_dict[name]
        else:
            name_idx = len(ing_dict.keys())
            ing_dict[name] = name_idx
        # 2-4-3. 재료별 레시피에 포션 레시피 저장
        if recipe_idx not in graph[name_idx]:
            graph[name_idx].append(recipe_idx)
        # 2-4-4. 재료 종류와 갯수 저장
        temp_set.add(name_idx)
        temp[name_idx] += cnt
    recipe_order[potion_idx].append(temp_set)
    recipe_dict[potion_idx].append(temp)
# 3. 레시피 별 가격 정리
q = deque([i for i in range(1, N + 1)])
while q:
    # 재료 사전에서 다른 재료(포션)와 레시피 번호 가져오기
    name_idx = q.popleft()
    if graph.get(name_idx):
        for next_idx, recipe_idx in graph[name_idx]:
            if name_idx in recipe_order[next_idx][recipe_idx]:
                recipe_order[next_idx][recipe_idx].remove(name_idx)
            if not len(recipe_order[next_idx][recipe_idx]):
                total_cost = 0
                # 가격 계산
                for ing, cost in recipe_dict[next_idx][recipe_idx].items():
                    total_cost += ing_cost[ing] * cost
                # 최솟값 저장
                if ing_cost[next_idx] > total_cost:
                    q.append(next_idx)
                    ing_cost[next_idx] = total_cost

# 출력
if ing_dict.get('LOVE'):
    result = ing_cost[ing_dict['LOVE']]
    if result == float('inf'):
        print(-1)
    elif result > 1000000000:
        print(1000000001)
    else:
        print(result)
else:
    print(-1)
