'''
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

class Solution:
    def checkCompleteness(self, root):
        queue = deque([root])
        showNone = False

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node is None:
                    showNone = True
                    continue

                if showNone:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True

# Time: O(n)

