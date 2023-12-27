# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumHead = None
        cur = None
        carry = 0
        while l1 or l2 or carry:
            l1Val = 0
            if l1:
                l1Val = l1.val
                l1 = l1.next
            l2Val = 0
            if l2:
                l2Val = l2.val
                l2 = l2.next
            s = l1Val + l2Val + carry 
            sumNode = ListNode(s % 10)
            carry = s // 10
            if cur:
                cur.next = sumNode
                cur = cur.next
            else:
                sumHead = cur = sumNode
                
                
        return sumHead