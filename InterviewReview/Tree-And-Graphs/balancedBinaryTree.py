# Define Superbalanced: if the difference between the depths of any two leaf nodes is no greater than one
class BinaryTreeNode(object):

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

'''
Breakdown
    1. Simplifying the problem
    Requirement of "the difference between the depths of any two leaf nodes is no greater than 1"
    implies that we will have to compare the depths of all possible pairs of leaves.
        Very expensive operations -> if n leaves, there is O(n^2) possible pairs of leaves
    
    Equivalent(simplifying) problem:
        * The difference between the min leaf depth and the max leaf depth is 1 or less
        * There are at most two distinct leaf depths, and they are at most 1 apart
    
    2. To get leaves and measure their depths, we have to traverse the tree somehow -> What methods do we know for traversing a tree?
        1. DFS (better in this case since our algorithm could short-circuit and return False as soon as it finds two leaves with depths more than 1 apart)
        2. BFS
'''

'''
We do DFS walk through the tree, keep tracking of the depth as we go. When we found a leaf, we add its depth
to a list of depths if we haven't seen the depth already.

Two ways to figure out whether the tree is unbalanced or not:
    * There are more than 2 different leaf depths
    * There are exactly 2 leaf depths and they are more than 1 apart
'''
class Solution:
    def __init__(self):
        pass

    def is_balanced(self, tree_root):
        if tree_root is None:
            return True

        depths = []

        # a stack stores (node, depth)
        nodes = []
        nodes.append((tree_root, 0))

        while len(nodes):
            # Pop a node and its depth from the top of the stack
            node, depth = nodes.pop()

            # Reach a leaf
            if not node.left and not node.right:
                if depth not in depths:
                    depths.append(depth)

                    if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                        return False
            else:
                if node.left:
                    nodes.append((node.left, depth+1))
                if node.right:
                    node.append((node.right, depth+1))
        return True

'''
O(n) time and space where n is the number of nodes.

nodes will hold at most d nodes where d is the depth of the tree O(d)
In a balanced tree, d is O(log(n)) and the more unbalanced the tree gets, the closer d gets to n

'''