import sys
from collections import deque
sys.setrecursionlimit(100010)
input = sys.stdin.readline

n, q = map(int, input().split())
parent = [int(input()) for _ in range(n-1)]
parent.insert(0, 0)
parent.insert(1, 1)
color = [int(input()) for _ in range(n)]
color.insert(0,0)

queries = [tuple(map(int, input().split())) for _ in range(q + n - 1)]

ans = deque()

sets = [set([color[i]]) for i in range(n+1)]

roots = [i for i in range(n+1)]

def find(v):
    if roots[v] == v:
        return v
    roots[v] = find(roots[v])
    return roots[v]


for cmd, node in reversed(queries):
    if cmd == 1:
        # 합치기
        # 부모 노드와 합친다. (union find)
        r_node = find(node)
        r_p_node = find(parent[node])
        roots[r_node] = r_p_node
        # 부모 노드와 자식 노드의 크기를 비교해 Small to Large 병합
        # 결과값으로는 부모set은 병합된 set을 가지고, 자식set은 빈 set을 갖도록 해준다.
        # 분기를 통해 부모셋을 항상 크게 한다.
        if len(sets[r_node]) > len(sets[r_p_node]):
            sets[r_node], sets[r_p_node] = sets[r_p_node], sets[r_node]
        # 자식의 모든 원소를 부모에 넣는다.
        # !!! 주의사항으로 set.union()을 사용하면 안된다는 점이 있다. !!!
        # 셋에 대해 직접 연산이 안이라 값 복사 + 연산 수행이라 m + n의 시간이 걸린다.
        # 고로 set.union()사용시 Small to Large 테크닉이 전혀 사용되지 않는다고 볼 수 있다.
        while sets[r_node]:
            sets[r_p_node].add(sets[r_node].pop())
    else:
        # ans에 출력값 넣기
        r_node = find(node)
        ans.append(len(sets[r_node]))

while ans:
    print(ans.pop())