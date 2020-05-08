'''
My soln
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates) #no.of pairs of ordinates
        if n==2:
            return True
        
        #variables: m=slope, c=y-intercept
        
        if not (coordinates[1][0]-coordinates[0][0]):
            m= 'inf'
            #slope inf indicates line is parallel y axis that is its all x co-ordinates must be same.
            x=coordinates[0][0]
            for i in range(1,n):
                if coordinates[i][0]!=x:
                    return False
            return True   
            
        else:
            m=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0]) #m=y2-y1/x2-x1
            c=coordinates[1][1]-m*coordinates[1][0] #since y=mx+c i.e. c=y-m*x
            for i in range(2,n):
                if c!=(coordinates[i][1]-m*coordinates[i][0]):
                    return False

            return True

'''
48 ms
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:  # general case
            return len(set([(coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0]) for i in range(len(coordinates) - 1)])) == 1
        except: # check vertical line
            return len(set([(coordinates[i+1][0] - coordinates[i][0]) for i in range(len(coordinates) - 1)])) == 1


'''
fast soln 44 ms
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0]-coordinates[1][0] == 0:
            m = 0
        else:
            m = (coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        c = coordinates[0][1] - m*coordinates[0][0] 
        
        for i in range(2,len(coordinates)):
            if coordinates[i][1] != m*coordinates[i][0] + c:
                return False
        return True


'''
fastest soln 40 ms
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n < 2:
            return False
        if n == 2:
            return True
        xs = [coordinates[i][0] for i in range(n)]
        
        if max(xs) == min(xs): 
            return True
        
        i = 1
        while coordinates[i][0] == coordinates[1][0]:
            i += 1
                          
        k = (coordinates[i][1]-coordinates[0][1]) /(coordinates[i][0]-coordinates[0][0])
        b = coordinates[0][1] - k * coordinates[0][0]
        
        for i in range(2,n):
            if abs(coordinates[i][1] - k * coordinates[i][0] - b) > 0.0001:
                return False
        
        return True
