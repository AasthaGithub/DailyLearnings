'''
24 ms counter 
'''
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        l = Counter(s)
        m = ''
        for i,v in (sorted(l.items(), key = lambda item: item[1],reverse=True)):
             print(i,v)
             m += i*v
        return m
        
 #32 ms

        res = ''
        for time, value in counter_obj.most_common():
            res += time * value
        return res
        
        
        
'''
fastest 20 ms
'''

import collections 
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        counterMap = collections.Counter(s)
        res = ''
        hq = []
        for char, freq in counterMap.items():
            heapq.heappush(hq, (-freq, char))

        while hq:
            freq, char = heapq.heappop(hq)
            res += -freq*char
            
        return res
