# 19. Remove Nth Node From End of List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        back_ptr = None
        forward_ptr = head
        for i in range(n - 1):
            forward_ptr = forward_ptr.next

        while forward_ptr.next is not None:
            if back_ptr is None:
                back_ptr = head
            else:
                back_ptr = back_ptr.next
            forward_ptr = forward_ptr.next

        if back_ptr is None:
            head = head.next
        else:
            back_ptr.next = back_ptr.next.next

        return head



#Improve test code
def test(n):
    head = ListNode(0)
    prevNode = head
    curNode = ListNode(1)
    prevNode.next = curNode

    prevNode = curNode
    curNode = ListNode(2)
    prevNode.next = curNode

    prevNode = curNode
    curNode = ListNode(3)
    prevNode.next = curNode

    s = Solution()
    new_head = s.removeNthFromEnd(head, n)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
    print("//")

test(1)
test(2)
test(3)
test(4)

def test2():
    head = ListNode(0)

    s = Solution()
    new_head = s.removeNthFromEnd(head, 1)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
    print("//")

test2()