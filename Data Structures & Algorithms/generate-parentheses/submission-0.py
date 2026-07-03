class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)

            if open_n < n:
                backtracking(open_n+1, closed_n, path+'(')
            
            if closed_n < open_n:
                backtracking(open_n, closed_n+1, path+')')

        backtracking(0,0,'')

        return res





        