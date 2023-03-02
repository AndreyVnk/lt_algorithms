'''Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.'''

class Solution:
    def construct(self, grid):
        return self.build(grid, 0, 0, len(grid))

    def sameValue(self, grid, x, y, sidelegth):
        value = grid[x][y]
        for i in range(x, x + sideLength):
            for j in range(y, y + sideLegth):
                if grid[i][j] != value:
                    return False
        return True

    def build(self, grid, x, y, sideLength):
        if self.sameValue(grid, x, y, sideLength):
            return Node(grid[x][y], True)

        root = Node(0, False)
        newSideLength = sideLength // 2
        root.topRight = self.build(grid, x, y, newSideLength)
        root.topLeft = self.build(grid, x, y + newSideLength, newSideLength)
        root.bottomLeft = self.build(grid, x + newSideLength, y, newSideLength)
        root.bottomRight = self.build(grid, x + newSideLength, y + newSideLength, newSideLength)

        return root


