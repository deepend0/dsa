class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        prev = None
        while cur and cur.next:
            next = cur.next
            cur.next = next.next
            next.next = cur
            if prev:
                prev.next = next
            else:
                head = next
            prev = cur
            cur = cur.next
        return head
