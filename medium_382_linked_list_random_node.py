'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
'''
from random import randrange

class Solution:
    
    def __init__(self, head):
        self.head = head
        self.size = 0
        curr = self.head
        while curr:
            self.size += 1
            cur = cur.next

    def getRandom(self) -> int:
        rand = randrange(self.size)
        curr = self.head
        while rand:
            curr = curr.next
            rand -= 1
        return curr.val

# Time O(n + r), Space: O(1)

