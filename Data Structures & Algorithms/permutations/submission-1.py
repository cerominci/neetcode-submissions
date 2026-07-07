class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        permutation = []
        used = [False] * len(nums)

        def dfs():
            if len(permutation) == len(nums):
                output.append(permutation.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                permutation.append(nums[i])
                used[i] = True

                dfs()

                permutation.pop()
                used[i] = False

        dfs()
        return output