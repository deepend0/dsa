# 105. Construct Binary Tree from Preorder and Inorder Traversal
from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.inorderMap = { inorder[i] : i for i in range(len(inorder))}
        return self._buildTree(0, 0, len(preorder))

    def _buildTree(self, i, j, l):
        val = self.preorder[i]
        k = self.inorderMap[val]

        node = TreeNode(val)
        if k > j:
            #print("Left", i + 1, j, k - j)
            node.left = self._buildTree(i + 1, j, k - j)
        if k < j + l - 1:
            #print("Right", i + k - j + 1, k + 1, j + l - 1 - k)
            node.right = self._buildTree(i + k - j + 1, k + 1, j + l - 1 - k)
        return node



def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
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

#1
#2 3
#4 5 6 7

# preorder 1 2 4 5 3 6 7
# inorder 4 2 5 1 6 3 7

# 1
# null 2
# null null 3 4
# null null null null null 5 6 null
# preorder 1 2 3 5 4 6
# inorder 1 3 5 2 6 4

s = Solution()
node = s.buildTree([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
print(levelOrder(node))

node = s.buildTree([1, 2, 3, 5, 4, 6],[1, 3, 5, 2, 6, 4])
print(levelOrder(node))

node = s.buildTree([1],[1])
print(levelOrder(node))

node = s.buildTree([1,2,3,4,5,6],[6,5,4,3,2,1])
print(levelOrder(node))


#Runtime: 60 ms, faster than 96.68% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
#Memory Usage: 18.5 MB, less than 96.33% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.