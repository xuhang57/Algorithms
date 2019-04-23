class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

'''
Breakdown:
    A simplier version of the problem is: How would we find the largest element in a BST?
    (in-order travesal? Right-most node?)

    Naive way is to find the right most element -> start from root and step down right child pointer
    until we cannot anymore (right child is None) -> Sufficient?
    
    How can we adapt this approach to find the second largest element?

    First thought -> the parent of the largest element? -> but the rightmost node could have a left subtree

    So, how do we handle the rightmost node has a left subtree case?
     -> it is the largest item in that left subtree (which we could find using the find largest method)
    But this takes O(h) time where h is the height of the tree and O(h) space. How could we avoid the call stack space?

    Use iterative method (cur = cur.right)

'''

class Solution:
    def find_largest(self, root):
        cur = root
        while cur:
            if not cur.right:
                return cur.value
            
            cur = cur.right

    def find_second_largest(self, root):
        if (root is None) or (root.left is None and root.right is None):
            return
        cur = root
        while cur:
            if cur.left and not cur.right:
                return find_largest(cur.left)
            if(cur.right and not cur.right.left and not cur.right.right):
                return cur.value
            
            cur = cur.right
        
'''
Time: O(h) where h is the height of the tree
Space: O(1) space

"Simplify, solve, and adapt" strategy and breaking things into cases is another good strategy

'''

# Recursive approach
def find_largest(root):
    if root is None:
        raise ValueError("Tree must have at least 1 node")
    if root.right is not None:
        return find_largest(root.right)
    return root.value

def find_second_largest(root):
    if (root is None) or (root.left is None and root.right is None):
        return ValueError("Tree must have 2 nodes")
    
    # we are currently at the largest, we need to find the second largest when there is a left subtree
    if root.left and not root.right:
        return find_largest(root.left)
    
    # we are at the parent of largest , and the largest has no left substree
    if root.right and not root.right.left and not root.right.right:
        return root.value
    return find_second_largest(root.right)

