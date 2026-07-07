class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return output


        