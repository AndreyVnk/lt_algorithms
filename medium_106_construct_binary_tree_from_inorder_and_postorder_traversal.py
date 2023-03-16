'''
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)

        root.right = self.buildTree(inorder[idx + 1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder

        return root

# Time: O(n^2)

