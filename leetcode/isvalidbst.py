class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTSub(root, None, None)
        
    
    def isValidBSTSub(self, node: TreeNode, minNode: TreeNode, maxNode: TreeNode) -> bool:
        if minNode is not None:
            if minNode.val >= node.val:
                return False
        
        if maxNode is not None:
            if maxNode.val <= node.val:
                return False
                
        if node.left is not None:
            if not self.isValidBSTSub(node.left, minNode, node):
                return False
            
        if node.right is not None:
            if not self.isValidBSTSub(node.right, node, maxNode):
                return False
                
        return True