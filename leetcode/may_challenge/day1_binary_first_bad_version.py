# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        '''
            Search in array starting from left to right
            At the beginning there's whole array to be scanned
            so start from 0 until n-1
        '''
        if n==1:
            return 1
        if n==2:
            if isBadVersion(1):
                return 1
            else:
                return 2
        
        left=1
        right=n
        '''
            For improving time complexity upto
            O(log n)
            binary approach is considered
        '''
        while(left<right):  
            #i.e. when the array(left to right) actually exists or its len > 1
            mid=left+(right-left)//2 
            if isBadVersion(mid):
                '''
                if mid is bad version it may or may not be the first bad,
                but definitely the ones on the right aren't first bad versions so, 
                the right bound for search becomes the mid position
                '''
                right=mid
            else:
                '''
                if mid isn't bad version means the ones ahead it are also not bad
                so search only in right sub-array
                '''
                left =mid+1
        return left
        """
        :type n: int
        :rtype: int
        """