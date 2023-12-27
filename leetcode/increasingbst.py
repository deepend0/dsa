
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.increasingBST_arrange(root, None, None)
        return self.head
    
    def increasingBST_arrange(self, node, minParent, maxParent):
        
        if node.left is None:
            if minParent is not None:
                minParent.right = node
            else:
                self.head = node
        else:
            self.increasingBST_arrange(node.left, minParent, node)
            node.left = None
        
        if node.right is None:
            node.right = maxParent
        else:
            self.increasingBST_arrange(node.right, node, maxParent)