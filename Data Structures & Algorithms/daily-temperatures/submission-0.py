class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        k = 1

        for i, t in enumerate(temperatures):
            if stack:
                while stack and t > stack[-1][0]:
                    stackT, stackInd = stack.pop()
                    res[stackInd] = i-stackInd
            stack.append((t,i))
        return res
        