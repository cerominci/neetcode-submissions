class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(i):
            for nei in adj[i]:
                if nei not in visited:
                   visited.add(nei) 
                   dfs(nei)
            
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        return res
                



        