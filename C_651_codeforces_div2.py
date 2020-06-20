mod=1000000  #max no to check

#cumulative/prefix array
primeBool=[0]*(mod+1)

#special cases
primeBool[2]=1
#primeBool[1]=primeBool[0]=0

first_done=0

def calc_dp():
    global first_done,primeBool,mod
    if not first_done:
        for i in range(3,mod+1,2):
        	primeBool[i]=1
        for i in range(3,mod+1,2):
        	if primeBool[i]==1:
        		for j in range(i*i,mod+1,i):
        			primeBool[j]=0
        first_done=1

def isPrime(N):
    
    if primeBool[N]:
        return True
    return False

def solve(n):
    winner=1
    if n==1:
        return 0
    
    if isPrime(n-1):
            return winner
    
    for i in range(3,n//3,2):
        if n%i==0:
            divisors=i
            if isPrime(n//i):
                return winner
    try:                
        return max(solve(n-1),solve(n//divisors))      
    except:
        return solve(n-1)
        

calc_dp()
t=int(input()) 
for i in range(t):
    a=int(input())
    
    if solve(a)==1:
        print('Ashishgup')
    elif solve(a)==0:
        print('FastestFinger')
