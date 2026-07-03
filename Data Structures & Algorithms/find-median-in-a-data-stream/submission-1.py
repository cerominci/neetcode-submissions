import heapq

class MedianFinder:
    def __init__(self):
        # maxHeap stores the smaller half (as negatives), minHeap stores the larger half
        self.maxHeap = []  # Python heap is min-heap; store negatives to simulate max-heap
        self.minHeap = []  # normal min-heap
       
    def addNum(self, num: int) -> None:
        # Decide where to push first
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # Rebalance so that: len(minHeap) == len(maxHeap) or len(minHeap) == len(maxHeap)+1
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Ensure ordering invariant: every element in maxHeap ≤ every element in minHeap
        if self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            # swap the roots
            max_top = -heapq.heappop(self.maxHeap)
            min_top = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -min_top)
            heapq.heappush(self.minHeap, max_top)

    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap:
            raise ValueError("No numbers added yet")

        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2.0
        else:
            # minHeap always has the extra element when odd
            return float(self.minHeap[0])
