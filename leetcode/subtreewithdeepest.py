# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        tovisit = [(root, 1)]
        parents = []
        maxDepth = 0
        deepestParents = []

        while len(tovisit) != 0:
            par = tovisit.pop()
            while len(parents) > 0 and par[1] <= parents[-1][1]:
                parents.pop()
            parents.append(par)
            if par[0].left is not None:
                tovisit.append((par[0].left, par[1]+1))
            if par[0].right is not None:
                tovisit.append((par[0].right, par[1]+1))
            if par[0].left is None and par[0].right is None:
                if maxDepth < par[1]:
                    maxDepth = par[1]
                    deepestParents = [parents.copy()]
                elif maxDepth == par[1]:
                    deepestParents.append(parents.copy())

        for i in range(0, maxDepth):
            commonPar = deepestParents[0][-1*(i+1)][0]
            found = True
            for j in range(1, len(deepestParents)):
                if deepestParents[j][-1*(i+1)][0] != commonPar:
                    found = False
                    break
            if found:
                return commonPar

    def buildTree(self, arr):
        root = None
        if arr:
            root = TreeNode(arr[0])
            st = [(root, 0, 0)]
            while len(st) != 0:
                el = st.pop(0)
                #print(el[0].val, el[1], el[2])
                next_l = el[1] + 1
                next_e = el[2] * 2
                next_i = (2 ** next_l - 1) + next_e
                #print(next_i)
                if next_i < len(arr) and arr[next_i] is not None:
                    el[0].left = TreeNode(arr[next_i])
                    st.append((el[0].left, next_l, next_e))
                next_e += 1
                next_i += 1
                if next_i < len(arr) and arr[next_i] is not None:
                    el[0].right = TreeNode(arr[next_i])
                    st.append((el[0].right, next_l, next_e))
        return root


s = Solution()
root = s.buildTree([3,5,1,6,2,0,8,None,None,7,4])
print(s.subtreeWithAllDeepest(root))
root = s.buildTree([1])
print(s.subtreeWithAllDeepest(root))
