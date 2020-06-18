#A
def solve(step,a,b,n):
    if a>n or b>n:
        print(step)
        return
    if a>b:
        b+=a
        step+=1
        solve(step,a,b,n)
    else:
        a+=b
        step+=1
        solve(step,a,b,n)

t=int(input())
for _ in range(t):
    a,b,n=list(map(int,input().split()))
    solve(0,a,b,n)


#A fibonacci
T=int(input())
while(T):
    T-=1
    a,b,n=[int(x) for x in input().split()]
    c=0
    if a>b:
        a,b=b,a
    count=0
    while(c<=n):
        c=a+b
        a=b
        b=c
        count+=1
    print(count)
    
#B
import math
ip=int(input())
s=['c', 'o', 'd', 'e', 'f', 'o', 'r', 'c', 'e', 's']
print()
take=ip//90 +2
thiss=round(math.log(ip,take))
print(take)
print(thiss)
letter=thiss%10
doall=thiss//10 +1
start=''
ans=''
for i in s:
    start+=(i*doall)
for i in range(letter):
    ans+=start[i*doall: (i+1)*doall ]+s[i]
print(ans+start[letter*doall:])
print(start)



#C - Reference - Alex Wice

FAST_IO = 1
if FAST_IO:
    import io, sys, atexit
    rr = iter(sys.stdin.read().splitlines()).next
    sys.stdout = _OUTPUT_BUFFER = io.BytesIO()
    @atexit.register
    def write():
        sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
else:
    rr = raw_input
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split())
 
####
 
 
def solve(R, C, A, queries):
    isolated = [[False] * C for _ in xrange(R)]
    blinktime = [[-1] * C for _ in xrange(R)]
    
    for r in xrange(R):
        for c in xrange(C):
            v = A[r][c]
            friend = False
            if 0 <= r-1 < R and A[r-1][c] == v:
                friend = True
            elif 0 <= r+1<R and A[r+1][c] == v:
                friend = True
            elif 0 <= c-1<C and A[r][c-1] == v:
                friend=  True
            elif 0 <= c+1<C and A[r][c+1] ==v:
                friend = True
            if not friend:
                isolated[r][c] = True
 
    # For each isolated, find min distance to group
    # Can use bfs
    queue = []
    for r in xrange(R):
        for c in xrange(C):
            if not isolated[r][c]:
                queue.append([r, c])
                blinktime[r][c] = 0
    for r, c in queue:
        for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0 <= nr<R and 0<=nc<C and blinktime[nr][nc] == -1:
                blinktime[nr][nc] = blinktime[r][c] + 1
                queue.append([nr,nc])
 
    for r,c,p in queries:
        r-=1;c-=1
        t = blinktime[r][c]
        if t==-1: t = float('inf')
        if p <= t:
            print A[r][c]
        else:
            d = (p-t) % 2
            print A[r][c] ^ d
 
 
R, C, T = rrm()
A = []
for _ in xrange(R):
    A.append(map(int, rr()))
 
queries = [rrm() for _ in xrange(T)]
solve(R, C, A, queries)
