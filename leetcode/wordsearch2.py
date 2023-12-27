# 212. Word Search II

from typing import List

class Node:
    def __init__(self):
        self.word = None
        self.children = None

class Solution:

    def __init__(self):
        self.dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        self.m = 0
        self.n = 0
        self.board = None
        self.trie = None
        self.found = None


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.m = len(board)
        if self.m == 0 or len(words) == 0:
            return []
        self.n = len(board[0])
        self.board = board

        self.trie = [Node()]
        for word in words:
            self.trieAdd(word)

        self.found = set()

        for i in range(self.m):
            for j in range(self.n):
                self.findWords_dfs(i, j, self.trie[0].children)
        return [word for word in self.found]

    def findWords_dfs(self, x, y, nodes):
        if 0 <= x < self.m and 0 <= y < self.n and self.board[x][y] != "":
            ix = charToIndex(self.board[x][y])
            if nodes[ix]:
                if nodes[ix].word:
                    self.found.add(nodes[ix].word)
                if nodes[ix].children:
                    c = self.board[x][y]
                    self.board[x][y] = ""
                    for d in self.dirs:
                        if self.findWords_dfs(x + d[0], y + d[1], nodes[ix].children):
                            return True
                    self.board[x][y] = c

    def trieAdd(self, word):
        cur = self.trie
        l_ix = 0
        for c in word:
            if not cur[l_ix].children:
                cur[l_ix].children = [None for _ in range(26)]
            cur = cur[l_ix].children
            ix = charToIndex(c)
            if cur[ix] == None:
                cur[ix] = Node()
            l_ix = ix
        cur[l_ix].word = word


def charToIndex(c):
    return ord(c[0]) - 97


s = Solution()

# ABC
# DEF
# GHI
board = [["a", "b", "c"],["d","e","f"],["g", "h", "i"]]

print(s.findWords(board, ["abc", "cfi", "behg", "cfehg"]))
print(s.findWords(board, ["adi", "ceg", "abl"]))
print(s.findWords(board, ["abcfedghi"]))


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
print(s.findWords(board, ["oath","pea","eat","rain"]))


print(s.findWords([], ["oath","pea","eat","rain"]))
print(s.findWords(board, []))