"""
Basic BST implementation to showcase recursive search
"""
def search(root, target):
        if not root:
            return False
        
        if target > root.val:
            return search(root.right, target)
        
        elif target < root.val:
             return search(root.left, target)
        
        else:
             return True