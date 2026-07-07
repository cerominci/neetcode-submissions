class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        perm = []
        used = [False]*len(nums)

        def dfs():
            if len(perm) == len(nums):
                output.append(perm[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                perm.append(nums[i])
                used[i] = True

                dfs()
                perm.pop()
                used[i] = False
        dfs()
        return output