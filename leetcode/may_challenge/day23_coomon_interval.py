class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        combinedIntervals = sorted(A + B)
        intersection = []
        currentEnd = -1

        for startInterval, endInterval in combinedIntervals:
            if startInterval <= currentEnd:
                intersection.append([startInterval, min(currentEnd, endInterval)])
            currentEnd = max(currentEnd, endInterval)        
        return intersection


'''
132 ms fastest
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        a_i = 0
        b_i = 0

        while a_i < len(A) and b_i < len(B):
            start_a, end_a = A[a_i]
            start_b, end_b = B[b_i]

            if end_a < start_b:
                a_i += 1
            elif end_b < start_a:
                b_i += 1
            else:
                if end_a <= end_b:
                    a_i += 1
                else:
                    b_i += 1
                res.append([max(start_a, start_b), min(end_a, end_b)])
        return res
