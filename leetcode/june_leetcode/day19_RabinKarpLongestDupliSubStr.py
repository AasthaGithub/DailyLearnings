MODULO = 100000000487  # prime

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        ords = bytes(ord(c) - ord('a') for c in S)
        
        cumulatives = [0]
        for o in ords:
            cumulatives.append(
                ( cumulatives[-1] * 26 + o) % MODULO
            )

        def _duplicate(length):
            MULT = pow(26, length + 1, MODULO)
            hsh = cumulatives[length + 1]
            seen = {hsh}
            for start in range(1, len(S) - length):
                hsh = ((26 * hsh - MULT * ords[start - 1]) + ords[start + length]) % MODULO
                if hsh in seen:
                    return start
                seen.add(hsh)
            return None

        best = None
        best_len = -1
                
        left = 0
        right = len(S) - 1
        
        while right - left >= 2:
            middle = (left + right) // 2
            cand = _duplicate(middle)
            cand_len = middle + 1
            if cand is not None:
                if cand_len > best_len:
                    best = cand
                    best_len = cand_len
                    
                left = middle + 1
            else:
                right = middle - 1

        if best_len < left + 1:
            new_cand = _duplicate(left)
            if new_cand is not None:
                best = new_cand
                best_len = left + 1
                new_cand = _duplicate(right)
                if new_cand is not None:
                    best = new_cand
                    best_len = right + 1
        
        if best is None:
            return ''
        
        return S[best:best + best_len]
 
 
 #
 class Solution:
    def longestDupSubstring(self, s: str) -> str:
        '''
            O(n log n)
        '''
        hash_mod = 2 ** 63 - 1
        nums = [ord(c) - ord("a") for c in s]
        n = len(s)
        # nums.p()
        def rabin_karp_l(cl):
            '''
                change from rabin_karp
                test the substring of length l is duplicated in s.
                for example: abanana, there is duplicated str "ana".
            '''
            # l26 = (26 ** cl) % hash_mod
            l26 = pow(26, cl, hash_mod)
            cur = 0
            for i in range(cl):
                cur = (26 * cur + nums[i]) % hash_mod
            # (cl, cur).p()
            visited = {cur}
            for i in range(cl, n):
                cur = (cur * 26 + nums[i] - nums[i - cl] * l26) % hash_mod
                if cur in visited:
                    return i - cl + 1
                visited.add(cur)
            return -1
        # using binary search
        l, r = 0, n
        pos = 0
        while l < r:
            m = (l + r + 1) // 2
            cur = rabin_karp_l(m)
            # (m,cur).p()
            if cur > -1:
                l = m
                pos = cur
            else:
                r = m - 1
        # l.p()
        return s[pos:pos+l]
        
#
class Solution:
    def longestDupSubstring(self, S):
        A = [ord(c)-ord("a") for c in S]
        mod = 2**32

        # L: the length of the substring to search
        def search(L):
            cur = 0
            for i in range(L):
                cur = (cur * 26 + A[i]) % mod
            seen = {cur}
            p = pow(26, L, mod)
            for i in range(L,len(A)):
                cur = (cur * 26 + A[i] - A[i-L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        start, lo, hi = 0, 0, len(A)
        while lo < hi:
            mid = (lo+hi+1)//2
            pos = search(mid)
            if pos:
                start = pos
                lo = mid
            else:
                hi = mid - 1
        return S[start:start+lo]
