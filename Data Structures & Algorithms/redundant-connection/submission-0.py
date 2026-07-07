class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]


        def dfs(i, par):
            if i in visited:
                return True
            visited.add(i)
            for nei in adj[i]:
                if nei == par:
                    continue
                if dfs(nei,i):
                    return True
            return False

        
        for ai, bi in edges:
            adj[ai].append(bi)
            adj[bi].append(ai)
            visited = set()
            if dfs(ai,-1):
                return [ai,bi]
        return []
         
