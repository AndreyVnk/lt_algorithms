'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
'''

class Solution:
    def missingElem(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid - 1
        
        return l + k

# Time: O(logn), Space: O(1)

