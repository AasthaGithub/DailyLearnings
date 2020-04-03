def s(listy):
        l2=[l**2 for l in listy]
        return sum(l2)
def to_digit_list(n):
    while(n>0):
        digits=[]
        digits.append(n%10)
        n=n//10
    return digits
        
def isHappy(n):
    if n==1:
        return True

    digits=to_digit_list(n)
    if sum(digits)==1:
        return True

    count=0
    while count<n: 
        newdigit=s(digits)
        if isHappy(newdigit)==True:
            return True
        count+=1
    return False   

class Solution(object):
    def isHappy(self,n):
        if n==1:
            return True

        digits=to_digit_list(n)
        if sum(digits)==1:
            return True

        count=0
        while count<n: 
            newdigit=s(digits)
            if isHappy(newdigit)==True:
                return True
            count+=1
        return False      

        