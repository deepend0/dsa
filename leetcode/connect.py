# Definition for a Node.

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        visitQueue = []
        if root is not None:
            visitQueue.append((root, 1))

        while len(visitQueue) != 0:
            elem = visitQueue.pop(0)
            if len(visitQueue) != 0 and visitQueue[0][1] == elem[1]:
                elem[0].next = visitQueue[0][0]

            if elem[0].left is not None:
                visitQueue.append((elem[0].left, elem[1]+1))
            if elem[0].right is not None:
                visitQueue.append((elem[0].right, elem[1]+1))

        return root
