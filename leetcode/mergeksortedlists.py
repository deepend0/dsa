# 23. Merge k Sorted Lists
from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    #def __lt__(self, other):
    #    return self.val < other.val

import heapq

class MyListNode:
    def __init__(self, listNode):
        self.listNode = listNode

    def __lt__(self, other):
        return self.listNode.val < other.listNode.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    	cursors = [MyListNode(l) for l in filter(lambda l: l is not None, lists)]
    	heapq.heapify(cursors)
    	sortedHead = None
    	sortedCursor = None
    	while cursors:

    		minNode = heapq.heappop(cursors)

    		if sortedHead is None:
    			sortedHead = minNode.listNode
    			sortedCursor = sortedHead
    		else:
    			sortedCursor.next = minNode.listNode
    			sortedCursor = sortedCursor.next

    		if minNode.listNode.next is not None:
    			myNextNode = MyListNode(minNode.listNode.next)
    			heapq.heappush(cursors, myNextNode)

    	return sortedHead


s = Solution()

lists = []
listNode = ListNode(1)
lists.append(listNode)
listNode.next = ListNode(3)
listNode = listNode.next
listNode.next = ListNode(5)

listNode = ListNode(2)
lists.append(listNode)
listNode.next = ListNode(4)
listNode = listNode.next
listNode.next = ListNode(6)

merged = s.mergeKLists(lists)
while merged:
	print(merged.val, "\t")
	merged = merged.next
print()

lists = []
listNode = ListNode(1)
lists.append(listNode)
listNode.next = ListNode(2)
listNode = listNode.next
listNode.next = ListNode(3)

listNode = ListNode(4)
lists.append(listNode)
listNode.next = ListNode(5)
listNode = listNode.next
listNode.next = ListNode(6)

merged = s.mergeKLists(lists)
while merged:
	print(merged.val, "\t")
	merged = merged.next
print()


lists = []
listNode = ListNode(1)
lists.append(listNode)
listNode.next = ListNode(2)
listNode = listNode.next
listNode.next = ListNode(3)

listNode = ListNode(1)
lists.append(listNode)
listNode.next = ListNode(2)
listNode = listNode.next
listNode.next = ListNode(3)

merged = s.mergeKLists(lists)
while merged:
	print(merged.val, "\t")
	merged = merged.next
print()

lists = []
listNode = ListNode(1)
lists.append(listNode)
listNode.next = ListNode(4)
listNode = listNode.next
listNode.next = ListNode(7)

listNode = ListNode(2)
lists.append(listNode)
listNode.next = ListNode(5)
listNode = listNode.next
listNode.next = ListNode(8)

listNode = ListNode(3)
lists.append(listNode)
listNode.next = ListNode(6)
listNode = listNode.next
listNode.next = ListNode(9)

merged = s.mergeKLists(lists)
while merged:
	print(merged.val, "\t")
	merged = merged.next


merged = s.mergeKLists([])
while merged:
	print(merged.val, "\t")
	merged = merged.next
print()

merged = s.mergeKLists([None])
while merged:
	print(merged.val, "\t")
	merged = merged.next
print()