# merge sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
<<<<<<< HEAD

=======
        
>>>>>>> 5174d390d34663b975111ca3d9d44665ea4c34f1
        result = []
        while left and right:
            if left[0] > right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        if left or right:
            result += left or right

        return result
<<<<<<< HEAD

=======
    
>>>>>>> 5174d390d34663b975111ca3d9d44665ea4c34f1
# quicksort
def qiucksort(nums):

    if len(nums) < 2:
        return nums

    pivot = nums[len(nums) // 2]
<<<<<<< HEAD

=======
    
>>>>>>> 5174d390d34663b975111ca3d9d44665ea4c34f1
    low, same, high = [], [], []

    for num in nums:
        if num < pivot:
            low.append(num)
        elif num == pivot:
            same.append(num)
        elif num > pivot:
            high.append(num)

<<<<<<< HEAD
    return quicksort(low) + same + quicksort(high)

=======
    return quicksort(low) + same + quicksort(high) 
        
>>>>>>> 5174d390d34663b975111ca3d9d44665ea4c34f1
