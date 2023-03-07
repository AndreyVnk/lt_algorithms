'''
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
'''

class Solution:
    def minimumTrips(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = max(time) * totalTrips
        time.sort()

        def isFeasible(per):
            total = 0
            for num in time:
                total += per // num
                if total >= totalTrips:
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Time: O(logn + m), Space: O(1)

