import sys
input = sys.stdin.readline

# 원래는 데이터도 가져아합니다.
class Node:
    def __init__(self) -> None:
        # self.data = None
        # self.data = 'word' 처럼 데이터가 있을 때 그 단어가 있다고 판단하는 근거가 됩니다.
        self.kids = {}

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    # 입력의 한 줄씩 바로 data로 받음
    def add(self, data: str) -> None:
        data = data.split()
        size = int(data[0])
        now = self.root
        for i in range(1, size+1):
            # 자식 중 없다면 추가
            if data[i] not in now.kids.keys():
                now.kids[data[i]] = Node()
            # 자식으로 나감
            now = now.kids[data[i]]
        # now.data = 'APPLE BANANA KIWI' # 와 같이 저장하는 단계가 원래는 필요

# 트라이 자체구연은 조금 귀찮은 면이 있으므로
# dfs를 통해 트리를 탐색해주자
def dfs(depth: int, node: Node):
    keys = list(node.kids.keys())
    keys.sort()
    for key in keys:
        # ----...--단어
        print('--'*depth, end='')
        print(key)
        # 다음 자식으로 dfs
        dfs(depth + 1, node.kids[key])


def solution():
    trie = Trie()

    n = int(input())
    for _ in range(n):
        trie.add(input())

    dfs(0, trie.root)


if __name__ == "__main__":
    solution()