class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        def dfs(i, cur):
            if i == len(nums):
                out.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i+1,cur)
             
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i +=1
            cur.pop()
            dfs(i+1,cur)
        
        dfs(0,[])
        return out

