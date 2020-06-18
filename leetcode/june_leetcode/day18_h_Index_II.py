#fastest
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            idx = (l + r)//2
            if n - idx - 1 < citations[idx]:
                r = idx
            else:
                l = idx + 1
        return n - l
