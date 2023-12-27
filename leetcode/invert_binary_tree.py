#226. Invert Binary Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            invertedRoot = TreeNode()
            self.invertTreeSub(root, invertedRoot)
            return invertedRoot
        return None

    def invertTreeSub(self, node1, node2):
        node2.val = node1.val

        if node1.left:
            node2.right = TreeNode()
            self.invertTreeSub(node1.left, node2.right)

        if node1.right:
            node2.left = TreeNode()
            self.invertTreeSub(node1.right, node2.left)


def printTree_infix(node):
    if node:
        printTree_infix(node.left)
        print(node.val)
        printTree_infix(node.right)

s = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

printTree_infix(root)
print()
printTree_infix(s.invertTree(root))