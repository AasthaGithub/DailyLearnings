#720 ms
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def bfs(node):

            q = deque()
            q.append(node)
            visited[node] = 1
            level[node] = 0

            while q:
                curr = q.popleft()
                for neighbour in adjList[curr]:
                    if visited[neighbour] == -1:
                        level[neighbour] = level[curr]+1
                        visited[neighbour] = 1
                        q.append(neighbour)
                    else:
                        if level[neighbour] == level[curr]:
                            return False
            return True



        n = N+1
        adjList = [[] for _ in range(n)]
        level = [-1] * n
        visited = [-1]* n

        for src,dst in dislikes:
            adjList[src].append(dst)
            adjList[dst].append(src)


        for i in range(1,n):
            if visited[i]==-1:
                if not bfs(i):
                    return False
        return True        


'''
708 ms fastest
'''
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors, graph = [0]*(N+1), collections.defaultdict(list)
        for left, right in dislikes:
            graph[left].append(right)
            graph[right].append(left)
        for idx, n in enumerate(colors):
            if idx > 0 and n == 0 and not self.DFS(idx, colors, graph, 1):
                return False
        return True
    
    def DFS(self, idx, colors, graph, c):
        colors[idx] = c
        for nxt in graph[idx]:
            if colors[nxt] == c or colors[nxt] == 0 and not self.DFS(nxt, colors, graph, -c):
                return False
        return True
'''
716 ms
''
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for pair in dislikes:
            u, v = pair[0]-1, pair[1] - 1
            graph[u].append(v)
            graph[v].append(u)
        
        
        color = [0] * N   
        for i in range(N):
            if color[i] == 0 and not self.dfs(graph, color, i, 1):
                return False
        return True
                             
    def dfs(self, graph, color, node, col):
        color[node] = col
        for neigh in graph[node]:
            if color[neigh] == col:
                return False
            if color[neigh] == 0 and not self.dfs(graph, color, neigh, -col):
                return False
        return True  
        
#732 ms
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        pairs = collections.defaultdict(set)
        for a, b in dislikes:
            pairs[a].add(b)
            pairs[b].add(a)
        groupA = set()
        groupB = set()
        for i in range(N):
            if i + 1 not in groupA and i + 1 not in groupB:
                q = collections.deque([(i+1, 0)])
                groupA.add(i + 1)
                while q:
                    person, group = q.popleft()
                    new_group = groupA if group == 1 else groupB
                    curr_group = groupA if group == 0 else groupB
                    group ^= 1
                    for new_person in pairs[person]:
                        if new_person in curr_group:
                            return False
                        elif new_person not in new_group:
                            new_group.add(new_person)
                            q.append((new_person, group))
        return True
        
