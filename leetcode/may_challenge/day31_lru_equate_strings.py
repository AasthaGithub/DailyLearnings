#76 ms
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i < 0 or j < 0: return max(i, j) + 1
            return dp(i - 1, j - 1) if word1[i] == word2[j] else min(dp(i - 1, j), dp(i - 1, j - 1), dp(i, j - 1)) + 1

        return dp(len(word1) - 1, len(word2) - 1)

#84 ms

from functools import lru_cache
# lru_cache to reduce the repeated calls.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def minDist(str1, str2, m, n): 
            if m == 0: 
                return n
                # If second string is empty, remove all of first string 
            if n == 0: 
                return m 
                # If last char of two strings are same, ignore last chars.
            if str1[m-1]== str2[n-1]: 
                return minDist(str1, str2, m-1, n-1) 
                # Else, consider all three 
                # operations on last character of first string, recursively 
                # compute minimum cost for all three operations and take 
                # minimum of three values. 
            return 1 + min(minDist(str1, str2, m, n-1), # Insert 
                    minDist(str1, str2, m-1, n), # Remove 
                    minDist(str1, str2, m-1, n-1)) # Replace
        return minDist(word1, word2, len(word1), len(word2))
        
        
        
from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        
        @lru_cache(None)
        def dp(i, j):
            
            if i < 0: return j + 1
            if j < 0: return i + 1
            
            ans = None
            if word1[i] == word2[j]: return dp(i-1, j-1)
            else: return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1

            return ans
        
        return dp(l1-1, l2-1)

#fastest 36 ms
from collections import deque

class Solution:  
    def minDistance(self, word1: str, word2: str) -> int:
        
        visited = set()
        q = deque([(word1, word2, 0)])
        
        while q:
            w1, w2, dist = q.popleft()
            
            if (w1, w2) not in visited:
                visited.add((w1, w2))

                if w1 == w2:
                    return dist

                while w1 and w2 and w1[0] == w2[0]:
                    w1 = w1[1:]
                    w2 = w2[1:]

                dist += 1
                q.extend([(
                    w1[1:], w2[1:], dist), 
                    (w1, w2[1:], dist), 
                    (w1[1:], w2, dist)])
