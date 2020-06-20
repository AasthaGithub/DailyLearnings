def gcd(a,b): 
    if(b==0):
        #print(a)
        return a 
        
    if a==0:
        return b
    elif a>b:
        return gcd(b,a%b) 
    else:
        return gcd(a,b%a)

'''
Approach:
 recursively finding lcm of two no.s and next number in array
'''


def getSmallestDivNum(n):
    ans=1
    for i in range(2,n):
        for j in range(2,n+1):
            ans=max(gcd(i,j),ans)
    return ans
t=int(input()) 
for i in range(t):
    a=int(input())
    print(getSmallestDivNum(a))
