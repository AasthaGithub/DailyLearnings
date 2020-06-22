#fastest normal dict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for val in nums:
            if not val in dict: 
                dict[val] = 1
            else:
                dict[val] += 1
        
        for k,v in dict.items():
            if v == 1:
                return k

#counter approach                
        # mathematical : return (sum(list(set(nums)))*3-sum(nums))//2
        #return numsCounter.most_common()[-1][0] 
        
        
#masking approach
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
           def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        
        for num in nums:
            one = ~two & (one ^ num)
            two = ~one & (two ^ num)
            
        return one

#masking alternative
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0        
        # compute single number by bit masking
        for bit_shift in range(32):            
            sum = 0            
            for number in nums:                
                # collect the bit sum
                sum += ( number >> bit_shift ) & 1
            # Extract bit information of single number by modulo
            # Other number's bit sum is removed by mod 3 (i.e., all other numbers appear three times)
            single_num |= ( sum % 3 ) << bit_shift
        if ( single_num & (1 << 31) ) == 0:
            return single_num
        else:
		# handle for negative number
            return -( (single_num^(0xFFFF_FFFF))+1 )
