import sys
from collections import deque
input = sys.stdin.readline

root = None

class Node:
    def __init__(self) -> None:
        self.word = None
        self.kids = {}
    
    def __repr__(self) -> str:
        return f"{self.word if self.word is not None else ''}{' : ' if self.word is not None else ''}{repr(self.kids)}"

def bfs():
    q = deque()
    ans = 0

    for startK, startV in root.kids.items():
        q = deque()
        q.append((startV, 1))

        while q:
            sep = False
            tree, dist = q.popleft()
            if tree.word != None:
                ans += dist
                dist += 1
                sep = True
            if len(tree.kids) == 1:
                for nextK, nextV in tree.kids.items():
                    q.append((nextV, dist))
            else:
                for nextK, nextV in tree.kids.items():
                    q.append((nextV, dist + (1 if not sep else 0)))

    return ans



while True:
    line = input()
    if line == '':
        break
    n = int(line)
    words = [input().strip() for _ in range(n)]

    root = Node()

    for word in words:
        now = root
        for letter in word:
            if letter not in now.kids.keys():
                now.kids[letter] = Node()
            now = now.kids[letter]
        now.word = word
    
    total = bfs()
    print(f'{total/n:.2f}')