class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1,1

        for num in nums:
            tmp = num*curMax
            curMax = max(num,num*curMax,num*curMin)
            curMin = min(num,tmp,num*curMin)
            res = max(res, curMax)

        return res
        