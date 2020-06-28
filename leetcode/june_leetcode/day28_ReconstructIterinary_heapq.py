#using heapq
class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		# graph
		g = defaultdict(lambda:[])
        #heapq q= ["JFK":["ATL","SFO"]]
		for u,v in tickets:
			# to maintain sort heap
			heapq.heappush(g[u],v)
		ans = []
    
		def go(s):
			# check if  any airport need to travel from cur airport
			while g[s]:
				a = heapq.heappop(g[s])
				# lets fly to a new airport
				go(a)			
			# current journey has no next flight anymore
			ans.append(s)
		
		# Starting the journey
		go("JFK")		
		# return with reversing the visited ans
		return ans[::-1]
    
#fastest
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#### By Euler path using DFS
        self.graph = collections.defaultdict(list)
        for frm,to in tickets:
            self.graph[frm].append(to)
            
        for k,v in self.graph.items():
            v.sort()
        
        self.ans = []
        self.DFS("JFK")
        return self.ans[::-1]
    
    def DFS(self,src):
        
        dest = self.graph[src]
        while dest:
            nextD = dest.pop(0)
            self.DFS(nextD)
        self.ans.append(src)
