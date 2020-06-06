'''
Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them,
therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[5,3],[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
After sorting:
[[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [5, 3], [4, 4]]

#another explanation:
lambda x: (x1,x2,x3....)
Compare the first element x1 of both tuples, if they are same, move on and decide outcome based on comparison of second element x2,
if still the same , compare x3,x4,x5....
So after we sort the list based on the (h,k).
We know that if we put short people in front of the list it woundn't bother those people with bigger h.
So what We need to do is just put the shorter people by k! 
because there must be no wrong in k, so when we insert (h,k) by k, it won't change the queue order.

O/P:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

#fastest 80 ms
class Solution:         
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda person: (person[0], -person[1]))
        people.reverse()
        queue = []
        for person in people:
            queue.insert(person[1],person)
        return queue

#comparison- customised sorting 
from functools import cmp_to_key

class Solution:
def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    people.sort(key=cmp_to_key(self.compareHeight))
    for i in range(len(people)-1,-1,-1):
    '''
    shift the items backwards according to the second index, 
    iterate in reverse order to prevent "cancelling" the previous shifting
    '''
        temp = people.pop(i)
        people.insert(i+temp[1],temp)
    return people

def compareHeight(self, a, b):
    #sort the list according to height, if height is the same, sort by the second index in reverse order
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    else:
        if a[1]>b[1]:
            return -1
        else:
            return 1
