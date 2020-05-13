'''
Fastest 20 ms- Stack and keep a check over last ele of stack
'''
class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        
        # Construct a monotone increasing sequence of digits
        for n in num:
            while k and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        
        
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        stack = stack[:-k] if k else stack
        
        
        # trip the leading zeros
        return "".join(stack).lstrip('0') or "0"



'''
moderate -mine
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k == len(num):
            return "0"
        
        out = []
        for i in range(len(num)):
            while k and out and out[-1] > num[i]:
                out.pop()
                k -= 1
            out.append(num[i])
            
        while k:
            out.pop()
            k -= 1
            
        return str(int(''.join(out)))

'''
First, we have to understand the problem and take a look at the test cases. When we look at the sample test cases and their answers, what pattern do we notice?

1432219 -> 1219, deleting 4,3,2

We notice that we delete a number when the next number is smaller. For example, we delete 4 because 3 comes after it, 3 because 2 comes after it, and 2 because 1 comes after it. In other words, we want to create an output that always deletes the larger number of at most k decreasing pairs.

To implement, we can do that through this code:

        out = []
        for i in range(len(num)):
            while k and out and out[-1] > num[i]:
                out.pop()
                k -= 1
            out.append(num[i])
We create an array that holds our current output. Every iteration through num, we add the element. However, in order to delete the larger number of each decreasing pair, we need a while loop to continuously check that the last element we added isn't larger than our current number. Why do we need the while loop instead of just checking nums[i] > nums[i+1]? Well consider the following example:

[0,2,3,4,1]

If we want to remove all decreasing pairs, using only nums[i] > nums[i+1] will result in [0,2,3,1] (only the last pair detected). However, this is incorrect, because 3 > 1. Instead, we need to continuously check our output array to make sure the last element we put in also fulfills this condition:

num[i]=0:    out = [0]                # add 1 becausec out is initially empty
num[i]=2:    out = [0,2]              # add 2, because 1<2
num[i]=3:    out = [0,2,3]            # etc.
num[i]=4:    out = [0,2,3,4]
num[i]=1:    out = [0,2,3,4]          # UH OH, 1<4! time to pop out 4
                    out = [0,2,3]     # UH OH, 1<3! pop out 3
					out = [0,2]       # etc.
					out = [0]         # finally, 1 > 0, so don't pop out 0
					out = [0,1]       # add 1
This is the key algorithm, so study it carefully. If you want more practice, check out Merge Intervals and Sliding Window Maximum, which use the same technique. Notice that out is ALWAYS increasing (i.e. sorted), since there are no pairs that are decreasing. This is called a monotonic stack/queue, and is a very important concept.

If we still have some k left after going through the entire array, just remove the last element until k is zero. We want to remove the biggest elements, and those are at the end of the output array:

        while k:
            out.pop()
For example, take [1,2,3], k=1. [1,2,3] is already sorted, so there are no decreasing pairs. Instead, we can just remove the last element 3, since the last element is guaranteed to be the maximum (remember, the output array is sorted by this point!). If we have k=2, then we need to remove 2 as well, by the same logic.

Finally, convert output array to a string with no leading zeroes. We can do that by converting array->string->int->string.

return str(int(''.join(out)))
'''



'''
Least Space Soln
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        
        changed = False
        while k > 0:
            for i in range(len(num) - 1):
                if num[i] > num[i+1]:
                    num = num[:i] + num[i+1:]
                    changed = True
                    break
                    
            if not changed:
                num = num[:-1]
            k -= 1
            changed = False
            
        i = 0
        while i < len(num) - 1 and num[i] == '0':
            i += 1
            
        return num[i:]
