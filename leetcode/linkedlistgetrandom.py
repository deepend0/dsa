from random import randint

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if self.head is None:
            return None
        
        current = self.head
        
        i = 0
        
        while current is not None:
            if randint(0, i) == 0:
                result = current.val
            current = current.next
            i += 1
            
        return result
    
head = ListNode(1)
curnode = head
nextnode = ListNode(2)
curnode.next = nextnode
curnode = nextnode
nextnode = ListNode(3)
curnode.next = nextnode
curnode = nextnode

sol = Solution(head)
print(sol.getRandom())


