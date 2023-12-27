# 102. Binary Tree Level Order Traversal

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_queue = [(root,0)]

        level_order = []
        current_level = -1
        if root:
            while node_queue:
                node_elem = node_queue.pop(0)
                if node_elem[1] > current_level:
                    level_order.append([])
                    current_level = node_elem[1]

                level_order[-1].append(node_elem[0].val)

                if node_elem[0].left:
                    node_queue.append((node_elem[0].left, node_elem[1]+1))
                if node_elem[0].right:
                    node_queue.append((node_elem[0].right, node_elem[1]+1))

        return level_order


s = Solution()


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)


head2 = TreeNode(1)
head2.left = TreeNode(2)
head2.right = TreeNode(3)
head2.left.left = TreeNode(4)
head2.left.left.left = TreeNode(5)
head2.right.right = TreeNode(6)
head2.right.right.right = TreeNode(7)


print(s.levelOrder(None))
print(s.levelOrder(head))
print(s.levelOrder(head2))
