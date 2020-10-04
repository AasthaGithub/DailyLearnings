'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true: 0 <= i, j < nums.length, i != j, a <= b, b - a == k

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
'''

#fastest w/o  counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
                
            return len([num for num in counts if counts[num] > 1])
                
        s = set(nums)
        total = 0
        for num in s:
            if num + k in s:
                total += 1
                
        return total
        
class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        pairs = set() # store pairs as {(a,b), a <= b} so they're unique
        seen = set()
        for n in nums:
            if n-k in seen:
                pairs.add((n-k, n))
            if n+k in seen:
                pairs.add((n, n+k))
            seen.add(n)
        return len(pairs)        
        
# 2 pointers approach
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        left = 0
        right = 1

        result = 0

        while (left < len(nums) and right < len(nums)):
            if (left == right or nums[right] - nums[left] < k):
                # List item 1 in the text
                right += 1
            elif nums[right] - nums[left] > k:
                # List item 2 in the text
                left += 1
            else:
                # List item 3 in the text
                left += 1
                result += 1
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1

        return result
