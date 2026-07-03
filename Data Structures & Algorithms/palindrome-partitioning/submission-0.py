class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output, cur = [], []

        def dfs(i):
            if i >= len(s):
                output.append(cur.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPali(s, i, j):
                    cur.append(s[i: j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return output
               

    def isPali(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

        