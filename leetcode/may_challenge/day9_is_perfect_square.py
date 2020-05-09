'''
Binary approach 16 ms
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while(r >= l):
            mid = int((l + r) / 2)
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                r = mid - 1
            else:
                l = mid + 1
        return False

'''
Brute Force approach 40 ms
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(num):
            if i*i > num:
                return False
            if i*i == num:
                return True



'''
24 ms helper fn
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 1
        r = num // 2
        def helper(l, r, num):
            while l <= r:
                mid = (l + r) // 2
                if mid * mid == num:
                    return True
                elif mid * mid < num:
                    return helper(mid+1, r, num)
                else:
                    return helper(l, mid-1, num)
            return False
        return helper(l, r, num)
        
'''
Binary approach 12 ms
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num //2
        while left <= right:
            mid = (left + right) // 2
            guess_sq = mid * mid
            if guess_sq == num:
                return True
            elif guess_sq > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
