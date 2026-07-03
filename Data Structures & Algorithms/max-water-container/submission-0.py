class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        width = len(heights) - 1

        area = min(heights[l],heights[r])*width
        while(l != r):
            if heights[l] < heights[r]:
                l +=1
                width -= 1
                area = max(area,min(heights[l],heights[r])*width)
            elif heights[r] < heights[l]:
                r -=1
                width -= 1
                area = max(area,min(heights[l],heights[r])*width)
            else:
                l +=1
                width -= 1
                area = max(area,min(heights[l],heights[r])*width)


        return area
    



            

        