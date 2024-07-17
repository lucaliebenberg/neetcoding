"""
Backtracking -> Tree Maze

Q: Determine if a path exists from the root of the tree to a lead node.
   It may not contain zeroes.
   Return: True / False

   Time complexity: O(n)
"""

def canReachLeaf(root):
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False