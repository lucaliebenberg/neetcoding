"""
Backtracking -> Tree Maze

Q: Determine if a path exists from the root of the tree to a lead node.
   It may not contain zeroes.
   Return: the value path

   Time complexity: O(n)
"""

def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False