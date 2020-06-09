#16 ms
class Solution:
    def isSubsequence(self, s, target):
        iter_target = iter(target)
        return all(char in iter_target for char in s)
        
#20 ms 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c == queue[0]:
                queue.popleft()
        return not queue
        
#28 ms
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        result =""
        for i in s:
            if i in t:
                result+=i
                
                t=t[t.index(i)+1:]
               
             
        if result== s:
            return True
