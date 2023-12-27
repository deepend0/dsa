#208. Implement Trie (Prefix Tree)
class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            ix = ord(c)-97
            if cur.children[ix] == None:
                cur.children[ix] = Node()
            cur = cur.children[ix]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            ix = ord(c)-97
            if cur.children[ix] == None:
                return False
            cur = cur.children[ix]
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            ix = ord(c)-97
            if cur.children[ix] == None:
                return False
            cur = cur.children[ix]
        return True
        

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

s = Trie()
print(s.search("pomegranade"))
s.insert("pomegranade")
print(s.search("pomegranade"))
print(s.search("pome"))
print(s.startsWith("pome"))
s.insert("pome")
print(s.search("pome"))
print(s.search("magic"))
print(s.startsWith("magic"))
