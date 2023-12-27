
def maxDepth(self, root) -> int:
    if root is None:
        return 0
    ldepth = 0
    rdepth = 0
    if root.left is not None:
        ldepth = self.maxDepth(root.left)
    if root.right is not None:
        rdepth = self.maxDepth(root.right)

    return max(ldepth, rdepth) + 1