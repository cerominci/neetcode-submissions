from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        output = [] 
        for x, y in points:
            distance = -sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, [distance, x, y])
            if len(maxHeap) > k :
                heapq.heappop(maxHeap)
            
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            output.append([x, y])
        return output