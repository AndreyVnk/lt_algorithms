# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        frequency = {}
        result = []
        self.findDuplicates(root, frequency, result)
        return result

    def findDuplicates(node, frequency, result):
        if not node:
            return '#'

        left = self.findDuplicates(node.left, frequency, result)
        right = self.findDuplicates(node.right, frequency, result)

        identificator = str(node.val) + ',' + left + ',' + right
        frequency[identificator] = frequency.get(identificator, 0) + 1
        
        if frequency[identificator] == 2:
            result.append(node)

        return identificator
