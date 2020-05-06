from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        n2=n/2
        nums_counter=Counter(nums)        
        for value, no_of_occurences in nums_counter.items():
            if no_of_occurences > n2:
                return value
'''
fastest python soln


by applying logic that  
    after sorting the array 
        the middle element of the array 
            would be majority element since it occurs more than n/2 times

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]            
'''
