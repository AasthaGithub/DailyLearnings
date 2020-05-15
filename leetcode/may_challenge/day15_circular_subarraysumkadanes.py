'''
fastest
'''
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curr_max = 0
        final_max = 0
        for i in A:
            curr_max += i
            if curr_max <= 0:
                curr_max = 0
            if final_max < curr_max:
                final_max = curr_max
        if final_max == 0:
            return max(A)
        
        curr_min = 0
        final_min = 0
        for i in A:
            curr_min += i
            if curr_min >= 0:
                curr_min = 0
            if final_min > curr_min:
                final_min = curr_min
        return max(final_max, sum(A) - final_min)

'''
fast
'''



class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:return 0
        mx=A[0]
        n=len(A)
        curr_sm=0
        
        # first normal kaden's ALgo. to get max subarray sum
        for i in range(n):   
            curr_sm +=A[i]
            if curr_sm>mx:
                mx=curr_sm
            if curr_sm<0:
                curr_sm=0
                
                
        # now considering circular subarray sum and if that is greater we change our mx accordingly.
    
        mxy=[A[0]]
        d_mx=A[0]
        for i in range(1,n):
            d_mx+=A[i]
            mxy.append(max(d_mx,mxy[-1])) # storing the max sum we get upto this index from start
        sm=0
        for i in range(n-1,1,-1):
            sm+=A[i]                # taking one by one no. from behind and adding the max sum we can get 
                                    # upto index (i-2) as we are not including (i-1)th index.
            mx=max(mx,sm+mxy[i-2]) 
        return mx
        
        
'''
fast
'''
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = curr_max = curr_min = 0
        maximum = float("-inf")
        minimum = float("inf")
        for num in A:
            total += num
            curr_max = max(0, curr_max) + num
            maximum = max(maximum, curr_max)
            curr_min = min(0, curr_min) + num
            minimum = min(minimum, curr_min)
        if total == minimum:
            return maximum
        return max(maximum, total - minimum)
        
'''
simple to understand
'''
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_so_far = min_so_far = min_ending_here = max_ending_here = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)    
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        if min_so_far == sum(A):
            return max_so_far
        else:
            return max(max_so_far,sum(A)-min_so_far)
            
'''
Editorial
''
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        array_sum = 0
        
        local_min_sum, global_min_sum = 0, float('inf')
        local_max_sum, global_max_sum = 0, float('-inf')
        
        for number in A:
            
            local_min_sum = min( local_min_sum + number, number )
            global_min_sum = min( global_min_sum, local_min_sum )
            
            local_max_sum = max( local_max_sum + number, number )
            global_max_sum = max( global_max_sum, local_max_sum )
            
            array_sum += number
        
        
        
        # global_max_sum denotes the maximum subarray sum without crossing boundary
        # arry_sum - global_min_sum denotes the maximum subarray sum with crossing boundary
        
        if global_max_sum > 0:
            return max( array_sum - global_min_sum, global_max_sum )
        else:
            # corner case handle for all number are negative
            return global_max_sum 
            
'''small'''
        t1=A[:]
        t2=A[:]
        c=0
        for i in range(1,len(A)):
            if t1[i-1]>0:     #find max one without circular
                t1[i]+=t1[i-1]
                c=1
            if t2[i-1]<0:     #find min one without circular
                t2[i]+=t2[i-1]
        if c==0:
            return max(A)
        return max(max(t1),(sum(A)-min(t2)))
