#206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev


def reverseAndPrint(head):
    s = Solution()
    reversedHead = s.reverseList(head)
    cur = reversedHead
    while cur:
        print(cur.val)
        cur=cur.next

head = ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next= ListNode(4)

reverseAndPrint(head)
reverseAndPrint(None)
reverseAndPrint(ListNode(1))

