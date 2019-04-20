class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

'''
BreakDown:
    One way is to come up with a way to confirm that a single node is in the valid
    place relative to its ancestors. Then if every node passes this test, our whole tree is a valid BST

What makes a given node "correct" relative to tis ancestors in a BST?
    1. if a node is in the ancestor's left substree, then its value must be less than that of the ancestor
    2. if a node is in the ancestor's right substree, then its value must be larger than that of the acestor

So we need to walk through the tree, the simplest ways to traveerse the tree:
    1. DFS (uses memory proportional to the depth of the tree)
    2. BFS (uses memory proportional to the breadth of the tree, levels)

Because the tree's breadth can as much as double each time it gets one level deeper (binary tree), DFS is likely
to be more space-efficeint than BFS, though they both have strictly both O(n) additional space in the worst case.

But we are not just storing the nodes themselves in the memory, we are also storing the value from each ancestor
and whether it should be less than or greater than the given node. Each node has O(n) ancestors (O(lgn) for a balanced binary tree)
, so that gives us O(n^2) additional memory cost (O(nlgn)). Is there a way to do better?

Rather than keeping tracking of every ancestor to check the inequalities, we just check the largest number
it must be greater than and the smallest number it must be less than

We could also check an in-order traversal of the tree is sorted.

'''
class Solution:
    def validBST(self, root):
        # start at the root, with a lower bound and upper bound
        node_and_bounds = [(root, -float('inf'), float('inf'))]

        # DFS
        while (len(node_and_bounds)):
            node, lower, upper = node_and_bounds.pop()

            # if this node is invalid, we return false right once
            if (node.value  <= lower) or (node.val >= upper):
                return False

            if node.left:
                # left node must be less than the current node
                node_and_bounds.append((node.left, lower, node.value))
            if node.right:
                # right node must be larger than  the current node
                node_and_bounds.append((node.right, node.val, upper))
            
        return True

'''
Time: O(n) where n is the number of nodes
Space: O(n), since we are doing a DFS, node_and_bounds will hold at most d nodes where d is the depth of tree

Greedy or "Divide and Conquer" approach.

'''