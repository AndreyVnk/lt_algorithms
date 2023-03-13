'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

class Solution:
    def symmetricTree(self, root):
        
        def symmtree(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return symmtree(left.left, right, left) and symmtree(left.right, right,left)
            return False

        return symmtree(root.left, root.right)

# Time: O(n)

