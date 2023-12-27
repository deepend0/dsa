# 100. Same Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p != None and q != None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

s = Solution()
head1 = TreeNode(1)

node1 = head1
node1.left = TreeNode(2)
node1.right = TreeNode(3)

head2 = TreeNode(1)
node2 = head2
node2.left = TreeNode(2)
node2.right = TreeNode(3)

head3 = TreeNode(1)
node3 = head3
node3.left = TreeNode(2)
node3.right = TreeNode(4)
head3 = TreeNode(1)

head4 = TreeNode(1)
node4 = head4
node4.left = TreeNode(2)
node4.right = TreeNode(3)
node4.left.left = TreeNode(4)

head5 = TreeNode(1)
node5 = head5
node5.left = TreeNode(2)
node5.right = TreeNode(3)
node5.left.right = TreeNode(4)

head6 = TreeNode(1)
node6 = head6
node6.left = TreeNode(2)
node6.right = TreeNode(3)
node6.left.left = TreeNode(4)

print(s.isSameTree(head1, head2))
print(s.isSameTree(head1, head3))
print(s.isSameTree(head1, head4))
print(s.isSameTree(head4, head5))
print(s.isSameTree(head4, head6))
print(s.isSameTree(None, None))