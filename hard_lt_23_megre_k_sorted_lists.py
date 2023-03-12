'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

# 1th approach (O(logn * n^2))
        nodes = []

        for head in lists:
            while head:
                nodes.append(head.val)
                head = head.next

        result = ListNode()
        curr = result
        for val in sorted(nodes):
            curr.next = ListNode(val)
            curr = curr.next

        return result.next

# 2nd approach (O(NlogN))
    def mergeTwoLists(l1, l2):
        head = ListNode()
        tail = head

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2

        return head.next

    n = len(lists)
    interval = 1
    while interval < n:
        for i in range(0, n - interval, interval * 2):
            list[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2

    return list[0]

