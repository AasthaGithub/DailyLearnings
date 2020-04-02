# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        i=0
        #moveahead=0
        while(i+1<len(intervals)):
            a=intervals[i].start
            b=intervals[i].end
            c=intervals[i+1].start
            d=intervals[i+1].end
            if (a==max(a,c) and b==max(b,d)):
                intervals[i].start=c
                intervals[i].end=d
                intervals[i+1].start=a
                intervals[i+1].end=b
            if not(max(a,c) > min(b,d)):
                intervals[i].start=min(a,c)
                intervals[i].end=max(b,d)
                del intervals[i+1]
                i=0
            
            else:
                i+=1
                #moveahead=1
            
        
        
        #for i in intervals:    
        #    print(i.start,i.end)    
		return intervals
'''
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, I):
        
        res = []
        I.sort(key=lambda i: i.start)
        for i in I:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res #working
'''