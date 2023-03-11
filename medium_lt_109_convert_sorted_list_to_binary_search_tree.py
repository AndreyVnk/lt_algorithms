'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.
'''

class Solution:
    def sortedListToBTS(self, head):
        if not head:
            return

        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow)

        if prev:
            prev.next = None
            root.left = self.sortedListToBTS(head)

        root.right = self.sortedListToBTS(slow.next)

        return root

# Time: O(NlongN), Space: O(1)

