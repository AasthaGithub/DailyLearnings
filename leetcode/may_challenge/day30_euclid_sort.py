#fastest 608 ms
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0] * x[0] + x[1] * x[1])
        return points[:K]
        
#612 ms

        def f(point):
            return  point[0]*point[0]+ point[1]*point[1]
        return sorted(points, key=f)[:K]
        
 class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda e: e[0]**2+e[1]**2)[0:K]       
