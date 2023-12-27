# 143. Reorder List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        ptr1 = head
        ptr2 = head
        while ptr2.next and ptr2.next.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next

        after_mid = ptr1.next

        ptr2 = after_mid
        ptr2_back = None
        while ptr2:
            ptr2_next = ptr2.next
            ptr2.next = ptr2_back
            ptr2_back = ptr2
            ptr2 = ptr2_next

        ptr1.next = None
        ptr1 = head
        ptr2 = ptr2_back

        while ptr2:
            ptr1_next = ptr1.next
            ptr2_next = ptr2.next
            ptr1.next = ptr2
            ptr2.next = ptr1_next
            ptr1 = ptr1_next
            ptr2 = ptr2_next


def print_node(node):
    while node:
        print(node.val)
        node = node.next


s = Solution()

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

print("orig")
print_node(node)
s.reorderList(node)
print("reordered")
print_node(node)


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)


print("orig")
print_node(node)
s.reorderList(node)
print("reordered")
print_node(node)


node = ListNode(1)

print("orig")
print_node(node)
s.reorderList(node)
print("reordered")
print_node(node)


node = ListNode(1)
node.next = ListNode(2)


print("orig")
print_node(node)
s.reorderList(node)
print("reordered")
print_node(node)