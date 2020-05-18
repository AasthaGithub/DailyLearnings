'''
fastest 36 ms
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
        
        d1 = {}
        for l in s1:
            if l in d1:
                d1[l] += 1
            else:
                d1[l] = 1
    
        d2 = {}
        for l in s2[:len(s1)]:
            if l in d2:
                d2[l] += 1
            else:
                d2[l] = 1
                
        if d1 == d2:
            return True
        
        for i in range(len(s2)-len(s1)):
            v_out = s2[i]
            if d2[v_out] == 1:
                del d2[v_out]
            else:
                d2[v_out] -=1

            v_in = s2[i+len(s1)]
            if v_in in d2:
                d2[v_in] += 1
            else:
                d2[v_in] = 1
            if d1 == d2:
                return True
                
        return False
        
        
'''
40 ms
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)
        s1Hash, s2Hash = 0, 0
        if s1Len > s2Len:
            return False
        
        for i in range(s1Len):
            s1Hash, s2Hash = s1Hash + hash(s1[i]), s2Hash + hash(s2[i])
        if s1Hash == s2Hash:
            return True
        for i in range(s1Len, s2Len):
            s2Hash += hash(s2[i]) - hash(s2[i-s1Len])
            if s2Hash == s1Hash:
                return True
        return False

'''
48 ms
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        counter1 = [0]*26
        counter2 = [0]*26
        for i in range(n):
            counter1[ord(s1[i])-ord('a')] += 1
        
        for j in range(m):
            if j >= n:
                counter2[ord(s2[j-n])-ord('a')] -= 1
            counter2[ord(s2[j])-ord('a')] += 1
            if counter1 == counter2:
                return True
        return False        
        
