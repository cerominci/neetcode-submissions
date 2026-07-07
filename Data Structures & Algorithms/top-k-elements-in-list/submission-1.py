class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        hp = []
        res = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            heapq.heappush(hp,(freq[num], num))
            if len(hp) > k:
                heapq.heappop(hp)

        while hp:
            res.append(heapq.heappop(hp)[1])

        return res

        