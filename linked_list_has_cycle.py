"""
Determine if the linked list contains a cycle
Time: O(n), Space: 0(1)
"""
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False