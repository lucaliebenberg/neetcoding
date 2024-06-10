# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# T O(n) and M O(n)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            # reversing the link between next node and head
            head.next.next = head
        # if head is first in the list, set it to null
        head.next = None
        
        return newHead