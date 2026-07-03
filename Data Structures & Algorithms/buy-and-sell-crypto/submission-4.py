class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        sell = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < sell:
                sell = prices[i]
            else:
                profit = max(prices[i]-sell, profit)
        return profit


        