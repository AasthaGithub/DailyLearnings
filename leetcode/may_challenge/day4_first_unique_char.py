'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

'''


#22 ms

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        Time: O(26*N), N = length of s
        Space: O(26) -> O(1)
        '''
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        
        return min(index) if len(index) > 0 else -1


#40 ms

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for char,val in c.items():
            if val==1:
                return s.index(char)
        return -1



#         # s=list(s)
#         # for a in  sorted(set(s), key=s.index):
#         #     if s.count(a)==1:
#         #         return s.index(a)
#         #     else:
#         #         continue
#         # return -1




# from collections import deque
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         d = {}
#         q = deque()
#         for i, x in enumerate(s):
#             d[x] = d.get(x, 0) + 1
#             if d[x] == 1:
#                 q.append((x, i))
#             while q and d[q[0][0]] > 1:
#                 q.popleft()
#         return -1 if not q else q[0][1]

