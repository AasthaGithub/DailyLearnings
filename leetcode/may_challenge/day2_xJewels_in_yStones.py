'''
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
'''



from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c=Counter(S)
        c=dict(c)
        ans=0
        for i in J:
            try:
                ans+=c[i]
            except:
                pass
        return ans
        