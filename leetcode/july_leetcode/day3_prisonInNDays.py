# for with & without pattern repeat knowledge: https://leetcode.com/problems/prison-cells-after-n-days/discuss/717929/Python-Easy-O(1)-Solution-Explained

#for any cell size & w/o knowing repeating pattern

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        states = {}
        for i in range(N):
            tmp = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in range(1, len(cells)-1)] + [0] 
            if (t := tuple(tmp)) in states:
                break
            states[t] = i
            cells[:] = tmp
        return sorted(states.keys(), key=states.get)[(N % len(states))-1]
        
#another generalized soln
#https://leetcode.com/problems/prison-cells-after-n-days/discuss/650581/Straightforward-Python3-solution-beat-80~90

#modularized
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        #pre = cells
       
        def findNext(pre):
            curr = [0] * len(cells)
            curr[0] = 0
            for j in range(1, len(cells)-1):
                #print(pre[j-1], pre[j+1])
                if pre[j-1] != pre[j+1]:
                    curr[j] = 0
                else:
                    curr[j] = 1
            curr[len(cells)-1] = 0
            return curr
       
        cycle = []
        state = findNext(cells)
        while state not in cycle:
            cycle.append(state)
            state = findNext(state)
           
        return cycle[(N - 1)%len(cycle)]
