# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        
        head = None
        last = None
        while cur1 or cur2:
            nextNode = None
            if cur1 is not None and (cur2 is None or cur1.val < cur2.val):
                nextNode = cur1
                cur1 = cur1.next
            else:
                nextNode = cur2
                cur2 = cur2.next
                
            if last:
                last.next = nextNode
                last = last.next
            else:
                head = last = nextNode
                
        return head
                