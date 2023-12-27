# 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has_cycle = False

        p1 = head
        p2 = None
        if head != None:
            p2 = head.next


        while p2 != None:
            if p1 == p2:
                has_cycle = True
                break
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next

        return has_cycle