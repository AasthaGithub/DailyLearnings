'''
76 ms
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        deg = [0]*numCourses
        
        for i, j in prerequisites:
            graph[j].append(i)
            deg[i] += 1
        
        queue = collections.deque([i for i, v in enumerate(deg) if v==0])
        
        while queue:
            cur_v = queue.popleft()
            for neighbor in graph[cur_v]:
                deg[neighbor] -= 1
                if deg[neighbor]==0:
                    queue.append(neighbor)
 
        return not sum(deg)
        
'''
80 ms
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(i, visit, graph):
                return False

        return True

    def dfs(self, i, visit, graph):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True

        visit[i] = -1
        for j in graph[i]:
            if not self.dfs(j, visit, graph):
                return False
        visit[i] = 1

        return True
        
#light
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n
