# To find where the target element should be inserted in the sorted list.
#lightest
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            m = l + int((r-l) / 2)
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        return l
        
#fastest 28 ms 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      
      lo, hi = 0, len(nums) - 1
      
      while lo < hi:
        mid = (lo + hi) // 2
        
        if nums[mid] == target:
          return mid
        
        elif nums[mid] < target:
          lo = mid + 1
        
        else:
          hi = mid
      
      if lo == len(nums) - 1 and target > nums[-1]:
        return len(nums) 
      return lo
      
#32 ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        
        while l <= h:
            m = l + (h-l) // 2
            
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                h = m-1
        
        return l
