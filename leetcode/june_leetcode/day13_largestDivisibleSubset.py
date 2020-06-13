#mine with bug
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        temp=[]
        curr=0
        maxi=0
        ans=[]
        if len(nums)==0 or 1:
            return nums
        else:
            for a in nums:
                if temp==[]:
                    temp=[a]
                    curr=1
                elif a%temp[-1]==0 or temp[-1]%a==0:
                    temp.append(a)
                    print('after append ', temp)
                    curr+=1
                    print(curr)
                    if curr>maxi:
                        maxi=curr
                        ans=temp
                else:
                    temp=[a]
                    curr=1
            return ans

#fastest
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        sort nums
        dynamic programming:
        dp = {}   key--num  val--length of largest divisible subset ending with num
        dp[num] = max(dp[x] num%x==0, x in nums) + 1
        sqrt(num), O(n*sqrt(max(nums))) + O(nlogn) (sort)        
        reconstruct the result list
        max_len = max(dp.values)  -- find the num         
        '''
        
        if not nums or  len(nums) == 0:
            return []
        nums = sorted(nums)
        dp = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                dp[1] = 1
                continue
            
            for j in range(1, int(sqrt(nums[i]))+1):
                tmp = nums[i] %  j
                if tmp == 0:
                    dp[nums[i]] = max(dp.get(j, 0) + 1, dp.get(nums[i]//j, 0) + 1, dp.get(nums[i], 1))
                    
        
        #  reconstruct the result
        rs  = list()
        max_len =  max(dp.values())
        while max_len > 0:
            for x in dp:
                if dp[x] == max_len:
                    rs.append(x)
                    break
            max_len -= 1
        return rs[::-1]

#244 ms        
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        buckets = [None, []]
        if len(nums) < 2:
            return nums
        max_len = 0
        for n in nums:
            atemp = max_len + 1
            placed = False
            while atemp > 0 and not placed:
                if atemp == 1:
                    buckets[1].append((None, n))
                    max_len = max(max_len, atemp)
                    placed = True
                else:
                    for _, p in buckets[atemp-1]:
                        if n % p == 0:
                            while len(buckets) - 1 < atemp:
                                buckets.append([])
                            buckets[atemp].append((p, n))
                            max_len = max(max_len, atemp)
                            placed = True
                            break
                atemp -= 1
        ans = [buckets[-1][0][1]]
        target = buckets[-1][0][0]
        for i in range(max_len-1, 0, -1):
            for d, p in buckets[i]:
                if p == target:
                    ans.insert(0, p)
                    target = d
                    break
        return ans  
        
#308 ms
from collections import defaultdict
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dic = {-1: set()}
        
        for num in nums:
            dic[num] = max([dic[n] for n in dic if num % n == 0], key = len) | {num}
            
        return list(max(dic.values(), key = len)) 
        
#lightest
from functools import reduce
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        pre = [-1] * len(nums)
        max_len = [1] * len(nums)
        max_len_idx = 0
        max_len_glob = 0
        for idx, i in enumerate(nums):
            for j in range(idx):
                if nums[j] % i == 0:
                    if max_len[j] + 1 > max_len[idx]:
                        max_len[idx] = max_len[j] + 1
                        pre[idx] = j
                        if max_len[idx] > max_len_glob:
                            max_len_glob = max_len[idx]
                            max_len_idx = idx
                
        result = []
        while pre and max_len_idx != -1:
            result.append(nums[max_len_idx])
            max_len_idx = pre[max_len_idx]

        return result
