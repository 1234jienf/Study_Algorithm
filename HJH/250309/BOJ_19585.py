import sys 
input = sys.stdin.readline


class Node:
    def __init__(self):
        self.word = None
        self.kids = {}


class Trie:
    def __init__(self):
        self.head = Node()
    
    def put(self, s: str):
        now = self.head
        for letter in s:
            if letter not in now.kids.keys():
                now.kids[letter] = Node()
            now = now.kids[letter]
        now.word = s
    

c, n = map(int, input().split())
colorT = Trie()
for _ in range(c):
    colorT.put(input().strip())

names = set()
for _ in range(n):
    names.add(input().strip())

def sol(word):
    idx = 0
    now = colorT.head
    while idx < len(word) and word[idx] in now.kids.keys():
        now = now.kids[word[idx]]
        idx += 1
        if now.word != None:
            if word[idx:] in names:
                return True
    return False

k = int(input())
for _ in range(k):
    word = input().strip()
    print('Yes' if sol(word) else 'No')