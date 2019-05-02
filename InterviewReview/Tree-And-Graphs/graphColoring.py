class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]

'''
Breakdown:
    Is it always possible to find a legal coloring with D+1 colors? Given each node has at most D neighbors.

    Since each node has at most D neighbors, and we have D + 1 colors , so if we look at any node, there is 
    always at least one color that's not taken by its neighbors.

    So the answer is yes, D+1 is always enough colors for a legal coloring.

    Brute Force:
        Try every possible combination of colors until we find a legal coloring:
            For each possible graph coloring
            If the coloring is legal, then return it
            Otherwise, move on to the next color

        Complexity: O(M * D^N) where N is the number of nodes, M is the number of edges
        each time we try a coloring, we have to check all M edges to see if the vertices at both ends have diff colors.
        

'''

class Solution:
    def graph_coloring(self, graph):
        pass

'''
Time:
Space:
'''

