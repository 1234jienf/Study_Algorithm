# 문제
## 우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다
## 이러한 촌수는 다음과 같은 방식으로 계산된다
## 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
## 나와 아버지, 아버지와 할아버지는 각각 1촌으로
## 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 
## 나와 아버지 형제들과는 3촌이 된다.

# 입력
## 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다.
## 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고,
## 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다
## 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
## 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.
## 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

# 출력
## 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다
## 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다
## 이때에는 -1을 출력해야 한다.

from collections import deque
# 사람 수 : n
n = int(input())
# 계산해야할 촌수의 사람관계
x,y = map(int,input().split())
# 관계의 수 : m
m = int(input())
ans = []
arr = [[0]* (n+1) for _ in range(n+1)]
visited = [0]* (n+1)

for i in range(m):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
    
def dfs(now,result,cnt):
    q = deque()
    q.append(now)
    visited[now] = 1
    while q:
        now = q.popleft()
        if now == result:
            ans.append(cnt)
            return   
        for i in range(1,n+1):
            if arr[now][i] == 1 and not visited[now][i]:
                q.append(i)
                dfs(i,result,cnt+1)

            

dfs(x,y,0)
if ans:
    print(ans[0])
else:
    print(-1)