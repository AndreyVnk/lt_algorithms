'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
'''

class Solution:
    def summNumbers(self, root) -> int:

        def dfs(node, num):
            if not node:
                return 0
            num += node.val
            if not node.left and not node.right:
                return num
            return dfs(node.left, num * 10) + dfs(node.right, num * 10)

        return dfs(root, 0)

# Time: O(n)

