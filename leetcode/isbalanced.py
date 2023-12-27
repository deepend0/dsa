class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        res = self.isBalancedSub(root)
        if res > 0:
            return True
        return False
        
    def isBalancedSub(self, node: TreeNode):
        ldepth = 0
        if node.left is not None:
            lres = self.isBalancedSub(node.left)
            if lres == 0:
                return 0
            else:
                ldepth = lres
        
        rdepth = 0
        if node.right is not None:
            rres = self.isBalancedSub(node.right)
            if rres == 0:
                return 0
            else:
                rdepth = rres
        
        if ldepth == rdepth or abs(ldepth-rdepth)==1:
            return max(ldepth, rdepth) + 1
        else:
            return 0
                