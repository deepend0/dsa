# 230. Kth Smallest Element in a BST

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root:
            return self.kthSmallestSub(root, k, 0)[1]
        return None

    def kthSmallestSub(self, node, k, l) -> int:
        order = l
        if node.left:
            orderValue = self.kthSmallestSub(node.left, k, l)
            if orderValue[1] is not None:
                return orderValue
            order = orderValue[0]

        order += 1
        if order == k:
            return (None, node.val)

        if node.right:
            orderValue = self.kthSmallestSub(node.right, k, order)
            if orderValue[1] is not None:
                return orderValue
            order = orderValue[0]

        return (order, None)

s = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

for i in range(1,9):
    print(s.kthSmallest(root, i))


print(s.kthSmallest(None, i))

print(s.kthSmallest(TreeNode(100), 1))
