class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        toVisit = [(original, 0)]
        parents = []

        current = None
        while len(toVisit) != 0:
            prev = current
            current = toVisit.pop()
            if prev is not None:
                for i in range(0, prev[1] - current[1] + 1):
                    print("pop")
                    parents.pop()

            print(current[0])
            parents.append(current[0])
            print(parents)
            if current[0] != target:
                if current[0].left is not None:
                    toVisit.append((current[0].left, current[1] + 1))
                if current[0].right is not None:
                    toVisit.append((current[0].right, current[1] + 1))
            else:
                break

        parentsdir = []
        for i in range(1, len(parents)):
            if parents[i-1].left == parents[i]:
                parentsdir.append('l')
            elif parents[i-1].right == parents[i]:
                parentsdir.append('r')

        clonedTarget = cloned

        for dir in parentsdir:
            if dir == 'l':
                clonedTarget = clonedTarget.left
            elif dir == 'r':
                clonedTarget = clonedTarget.right

        return clonedTarget

    def buildTree(self, arr):
        root = None
        if arr:
            root = TreeNode(arr[0])
            st = [(root, 0, 0)]
            while len(st) != 0:
                el = st.pop(0)
                next_l = el[1] + 1
                next_e = el[2] * 2
                next_i = (2 ** next_l - 1) + next_e
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

tree = s.buildTree([7,4,3,None,None,6,19])
target = tree.right
cloned = s.buildTree([7,4,3,None,None,6,19])
print(s.getTargetCopy(tree, cloned, target).val)


tree = s.buildTree( [8,None,6,None,5,None,4,None,3,None,2,None,1])
target = tree.right.right.right
cloned = s.buildTree( [8,None,6,None,5,None,4,None,3,None,2,None,1])
print(s.getTargetCopy(tree, cloned, target).val)


tree = s.buildTree( [1,2,3,4,5,6,7,8,9,10])
target = tree.left.right
cloned = s.buildTree( [1,2,3,4,5,6,7,8,9,10])
print(s.getTargetCopy(tree, cloned, target).val)
