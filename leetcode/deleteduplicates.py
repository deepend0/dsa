class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prevNode = None
        curNode = head
        curDuplicate = False
        
        while curNode and curNode.next:
            if curNode.val == curNode.next.val:
                curDuplicate = True
                if prevNode:
                    prevNode.next = curNode.next.next
                else:
                    head = curNode.next.next
                curNode = curNode.next
            else:
                if not curDuplicate:
                    prevNode = curNode
                curDuplicate = False
                curNode = curNode.next
                
        return head