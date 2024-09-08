n = int(input())
arr = tuple(map(int, input().split()))

checker = {}
sums = [0]

for i in range(n):
    if arr[i] not in checker.keys():
        checker[arr[i]] = []
    checker[arr[i]].append(i)
    sums.append(sums[-1] + arr[i])

ansSum = 0
ansCount = 0
for num, indexes in checker.items():
    # 마이너스가 배열 내에 없으니 가장 긴 인덱스가 아니면 최대합의 가능성이 없다
    ansCandidate = sums[indexes[-1] + 1] - sums[indexes[0]]
    if ansSum < ansCandidate:
        ansSum = ansCandidate
        ansCount = 1
    elif ansSum == ansCandidate:
        ansCount += 1

print(f'{ansSum} {ansCount}')