#dp & lightest
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(1, n+1):
            tmp = 0
            for j in range(1, i+1):
                tmp += dp[j-1]*dp[i-j]
            dp[i] = tmp
        return dp[-1]
#recursion v1
#it's natural to come up with the recursion idea.

    def numTrees_v0_recursion(self, n: int) -> int:
        
        @functools.lru_cache(maxsize=None)
        def helper( lo, hi ):
            if lo == hi: return 1
            return sum( helper(lo, iRoot) * helper(iRoot+1, hi) for iRoot in range(lo, hi) )
        
        return helper(0, n)
#recursion v2
#Then I find that the result of helper can be determined by the number of elements (ie. hi-lo )
#no matter what the elements are (ie. the value of lo or hi ). Here comes solution 2.

    def numTrees_v1_recursion(self, n: int) -> int:
        
        @functools.lru_cache(maxsize=None)
        def helper( num ):
            if not num: return 1
            return sum( helper(iRoot) * helper(num-iRoot-1) for iRoot in range(num) )
        
        return helper(n)
#DP
#Looking at solution 1, we can recognize the pattern that helper(n) is calculated using helper(i) for i = 0, 1, ..., n-1. This is obvious DP pattern.

    def numTrees_v2_dp(self, n: int) -> int:
        dp = [1] * (n+1)
        for index in range(2, n+1):
            dp[index] = sum( dp[i] * dp[index-1-i] for i in range(index))
        return dp[n]
# math
#After browsering discussion forum, I found that this is a catalan number. So we can directly calculate the answer mathematically.

    def numTrees_v3_catalan(self, n):   # Catalan Number  (2n)!/((n+1)!*n!)  
        return math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))
        
        
#top down approach: https://leetcode.com/problems/unique-binary-search-trees/discuss/703707/Python3-or-98-faster-or-Top-down-Dp-solution        
# another good explanation: https://leetcode.com/problems/unique-binary-search-trees/discuss/703049/Python-Math-oneliner-O(n)-using-Catalan-number-explained        
