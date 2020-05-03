'''
Ransom note from magazine string
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rl=len(ransomNote)
        ml=len(magazine)
        
        if ml<rl:
            return False        
        r=Counter(list(ransomNote))
        m=Counter(list(magazine))
        z=r-m
        #print(z)
        for i in z.values():
            if i!=0:
            # if a character would not be in magazine,
            #then its count wouldn't have been subtracted from counter
                return False
        return True
            
        
        