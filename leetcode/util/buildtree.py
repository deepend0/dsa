class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def buildTree(arr):
    root = None
    if arr:
        root = TreeNode(arr[0])
        st = [(root, 0, 0)]
        while len(st) != 0:
            el = st.pop(0)
            # print(el[0].val, el[1], el[2])
            next_l = el[1] + 1
            next_e = el[2] * 2
            next_i = (2 ** next_l - 1) + next_e
            # print(next_i)
            if next_i < len(arr) and arr[next_i] is not None:
                el[0].left = TreeNode(arr[next_i])
                st.append((el[0].left, next_l, next_e))
            next_e += 1
            next_i += 1
            if next_i < len(arr) and arr[next_i] is not None:
                el[0].right = TreeNode(arr[next_i])
                st.append((el[0].right, next_l, next_e))
    return root