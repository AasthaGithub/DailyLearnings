'''
time: 52 ms fastest
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2-sum(nums)


'''
time: 56 ms Binary Search Approach  
'''

##IMPPPP
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]

'''
time: 60 ms
'''
class Solution:
    """
    1  1  4  4  5  5  6  8  8
               mid .
    1  1  4  5  5  6  6  8  8  9
             .    
    """
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                halves_are_even = right - mid - 1
                if halves_are_even % 2 == 1:
                    left = mid + 2
                else:
                    right = mid - 1
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                halves_are_even = right - mid
                if halves_are_even % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 2
            else:
                return nums[mid]
        return -1
    
    def singleNonDuplicateBruteForce(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]
                


'''
time: 64 ms
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        t = nums[0]
        for i in range(1, len(nums)):
            t = t ^ nums[i]
        
        return t
