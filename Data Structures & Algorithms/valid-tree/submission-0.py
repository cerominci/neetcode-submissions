class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(i, parent):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == parent:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        return dfs(0,-1) and len(visit) == n
        
        