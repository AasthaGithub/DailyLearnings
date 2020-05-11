'''
Short 744 ms
'''
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1   
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1   




'''
Fastest 740 ms
'''
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
        
        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)
        
        for a,b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        
        for i in range(1, N+1):
            if(indegree[i] == N-1 and outdegree[i] == 0):
                return i
        
        return -1



'''
Fastest 736 ms
'''
class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1 and trust == []:
            return 1
        from collections import defaultdict
        d = defaultdict(int)

        for a, b in trust:
            d[b] += 1

        ans = []
        for key in d.keys():
            if d[key] == N - 1:
                ans.append(key)

        if len(ans) != 1:
            return -1
        else:
            for a, b in trust:
                if a == ans[0]:
                    return -1
            return ans[0]
