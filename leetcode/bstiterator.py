
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self._stack = [[root,None,0,0,0]]
        self._next = None

    def next(self) -> int:
        if self.hasNext():
            returnNext = self._next
            self._next = None
            return returnNext.val
        else:
            return None
        
    def hasNext(self) -> bool:
        while self._next is None:
            if len(self._stack) > 0:
                curElem = self._stack[-1]
                curNode = curElem[0]
                if curNode.left is not None and curElem[2] == 0:
                    self._stack.append([curNode.left, 'l', 0, 0, 0])
                elif curElem[3] == 0:
                    self._next = curNode
                    curElem[3] = 1
                    return True
                elif curNode.right is not None and curElem[4] == 0:
                    self._stack.append([curNode.left, 'r', 0, 0, 0])
                else:
                    self._stack.pop(-1)
                    if curElem[1] == 'l':
                        self._stack[-1][2] = 1
                    elif curElem[1] == 'r':
                        self._stack[-1][4] = 1
                    else:
                        return False
            return False
        else:
            return True
        