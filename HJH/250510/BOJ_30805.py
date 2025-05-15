from heapq import *

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ha = []
for i in range(n):
    heappush(ha, (-a[i], i))
hb = []
for i in range(m):
    heappush(hb, (-b[i], i))

def possible_heap_pop(heap, valid_idx):
    while heap:
        val, idx = heappop(heap)
        if idx >= valid_idx:
            return val, idx
    return 1, -1

aidx = 0
bidx = 0

ans = []

while ha and hb:
    max_a, idx_a = possible_heap_pop(ha, aidx)
    max_b, idx_b = possible_heap_pop(hb, bidx)
    while max_a != max_b:
        if max_a < max_b:
            max_a, idx_a = possible_heap_pop(ha, aidx)
        elif max_b < max_a:
            max_b, idx_b = possible_heap_pop(hb, bidx)
    if max_a == 1:
        break
    ans.append(-max_a)
    aidx = idx_a
    bidx = idx_b

print(len(ans))
print(*ans)