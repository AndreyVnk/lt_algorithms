'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(cap):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / cap)
            return hours <= h

        while l <= r:
            k = (l + r) // 2
            if catEat(k):
                res = k
                r = k - 1
            else:
                r = l + 1

        return res

# Time: O(log(max(arr)) * len(arr)), Space: O(1)

