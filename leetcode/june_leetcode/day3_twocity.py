'''
20 ms fastest
'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:        
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        n = len(costs)
        return sum(costs[i][0] for i in range(n//2)) + sum(costs[i][1] for i in range(n//2,n))
        
        
#mine 40 ms 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dep=[]
        ans=0
        n=len(costs)
        for i in range(n):
            costs[i].append(costs[i][0]-costs[i][1])
        costs.sort(key= lambda x:x[2]) 

        
        ans+=sum(costs[i][0] for i in range(n//2))
        ans+=sum(costs[i][1] for i in range(n//2,n))
        
        return ans
        
                
