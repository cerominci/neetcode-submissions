class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        chosen = [0]*len(nums)

        def dfs(cur,chosen):
            if len(cur) == len(nums):
                out.append(cur.copy())
                return

            for j in range(len(nums)):
                if not chosen[j]:
                    cur.append(nums[j])
                    chosen[j] = 1
                    dfs(cur,chosen)
                    cur.pop()
                    chosen[j] = 0

        dfs([],chosen)
        return out

        