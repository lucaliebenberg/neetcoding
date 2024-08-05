"""
Q: Find the middle of a linked list\
Time: 0(n), Space: O(1)
"""
def middleList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

