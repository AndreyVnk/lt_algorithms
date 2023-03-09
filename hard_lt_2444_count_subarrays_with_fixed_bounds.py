'''
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.
'''

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxL, int) -> int:
        n = len(nums)
        leftBound = -1
        lastMin, lastMax = -1, -1
        count = 0

        for i in range(n):
            if nums[i] >= minK and nums[i] <= maxK:
                lastMin = i if nums[i] == minK else lastMin
                lastMax = i if nums[i] == maxK else lastMax 
                count += max(0, min(lastMin, lastMax) - leftBound)
            else:
                leftBount = i
                lastMin = -1
                lastMax = -1

        return count

# Time O(n), Space O(1)

