# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# T O(n) and M O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # use of 2 pointers
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
