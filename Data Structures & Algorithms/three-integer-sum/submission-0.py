from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Sort the array first

        # Iterate with the first pointer 'i'
        for i in range(len(nums) - 2): # -2 because we need at least two more elements (l and r)
            # Skip duplicate values for 'i'
            # If current nums[i] is the same as the previous nums[i-1],
            # it means we've already considered this first element for triplets,
            # so skip it to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initialize two pointers for the rest of the array
            l = i + 1
            r = len(nums) - 1

            # Two-pointer approach
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum == 0:
                    # Found a triplet!
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicate values for 'l'
                    # Move 'l' forward as long as it points to the same value
                    # and 'l' is still less than 'r'
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Skip duplicate values for 'r'
                    # Move 'r' backward as long as it points to the same value
                    # and 'l' is still less than 'r'
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    # Move both pointers to the next unique elements
                    l += 1
                    r -= 1
                elif current_sum < 0:
                    # Sum is too small, need a larger value from the left
                    l += 1
                else: # current_sum > 0
                    # Sum is too large, need a smaller value from the right
                    r -= 1
        
        return res