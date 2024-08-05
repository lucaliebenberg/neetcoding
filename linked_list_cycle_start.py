"""
Determine if the linked list contains a cycle,
a return the beginnign of the cycle, otherwise
return null
Time: O(n), Space: 0(1)
"""
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
            break

    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow