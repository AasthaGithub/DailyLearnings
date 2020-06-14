#mine_ minor bug
def findCheapestPrice( n, flights, src, dst, k):
    # dp[i,j] stores the shortest path to j after i-th iteration
    # k+2 because we have k stops that means k vertices between start and stop that gives you k+1 edges
    # After k-th iteration bellman-ford gives you shortest path using at most k edges,
    # or in our case i-1 stops
    dp=[[float('inf')]*n]*(k+1)
    #this is long because dp[i-1, edge[0]] + edge[2] can actually be more than int.MaxValue 

    #dp[0][src] = 0

    for i in range(0,k+1):       

        dp[i][src] = 0
        for edge in flights:
            try:
                dp[i][edge[1]] = min(dp[i][edge[1]], dp[i-1][edge[0]] + edge[2])            
            except:
                pass
    if dp[k][dst] == float('inf'): 
        return -1 

    return dp[k][dst]
print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))


#64 ms
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
         # Build the adjacency matrix
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))
            
        # Shortest distances array
        distances = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        
        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]     
        
        while minHeap:
            
            cost, stops, node = heapq.heappop(minHeap)
            
            # If destination is reached, return the cost to get here
            if node == dst:
                return cost
            
            # If there are no more steps left, continue 
            if stops == K + 1:
                continue
             
            # Examine and relax all neighboring edges if possible 
            for nei, price in graph[node]:
                dU, dV, wUV = cost, distances[nei], price
                    
                    # Better cost?
                if dU + wUV < dV:
                    distances[nei] = dU + wUV
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                elif stops < current_stops[nei]:

                    #  Better steps?
                    current_stops[nei] = stops
                    heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))

        return -1 if distances[dst] == float("inf") else distances[dst]
        
#68 ms
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        #if src == dst:
            #return 0
        heap = [(0, 0, src)]
        stop = [sys.maxsize] * n
        stop[src] = 0
        distance = [sys.maxsize] * n
        distance[src] = 0
        frontier = collections.deque([src])
        edges = collections.defaultdict(list)
        for u, v, w in flights:
            edges[u].append((v, w))
        while heap:
            du, s, u = heapq.heappop(heap)
            if u == dst:
                return du
            
            if s == K + 1:
                continue
            for v, w in edges[u]:
                if distance[v] > du + w:
                    distance[v] = du + w
                    if stop[v] > s:
                        stop[v] = s
                    heapq.heappush(heap, (du + w, s + 1, v))
                elif stop[v] > s:
                    stop[v] = s
                    heapq.heappush(heap, (du + w, s + 1, v))
            
        return -1 if distance[dst] == sys.maxsize else distance[dst]
#simple
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # di
        mapp = defaultdict(dict)
        for s, d, p in flights:
            mapp[s][d] = p
            
        hp = []
        for d, p in mapp[src].items():
            heapq.heappush(hp, (p, d, 0))
        
        price = 0
        while hp:
            price, d, k = heapq.heappop(hp)
            if k>K:
                continue
            if d == dst:
                return price
            
            for nd, np in mapp[d].items():
                heapq.heappush(hp, (price+np, nd, k+1))
        
        return -1
