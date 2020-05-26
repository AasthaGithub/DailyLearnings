#800 ms 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total_sum = 0
        index = dict()
        max_length = 0
        index[0] = -1
        
        for i, num in enumerate(nums):
            if num == 0:
                total_sum -= 1
            else:
                total_sum += 1
            
            if total_sum in index:
                length1 = i - index[total_sum]
                if length1 > max_length:
                    max_length = length1
            
            else:
                index[total_sum] = i
        
        return max_length
            
            
'''
fastest 796 ms
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count1 = 0
        for i in range(len(nums)):
            if nums[i]:
                count1 += 1
        count0 = len(nums) - count1
        
        if count0 == count1:
            return len(nums)
        
        i, j = 0, len(nums) - 1
        more = int(count1 > count0)
        diff = abs(count1 - count0)
        
        left = [0]
        right = [len(nums)]
        diff1, diff2 = diff, diff
        for index in range(diff - 1, -1, -1):
            while diff1 > index:
                if nums[i] == more:
                    diff1 -= 1
                else:
                    diff1 += 1
                i += 1
            left.append(i)
            
            while diff2 > index:
                if nums[j] == more:
                    diff2 -= 1
                else:
                    diff2 += 1
                j -= 1
            right.append(j + 1)
        
        maxlen = right[-1] - left[0]
        for index in range(len(left)):
            maxlen = max(maxlen, right[-1 - index] - left[index])
        return maxlen
                
            
