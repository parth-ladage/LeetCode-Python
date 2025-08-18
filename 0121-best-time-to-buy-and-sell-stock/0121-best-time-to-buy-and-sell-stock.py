class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowPrice = float('inf')
        highPrice = 0

        for i in prices :
            lowPrice = min(lowPrice, i)

            currentPrice = i - lowPrice
            highPrice = max(highPrice, currentPrice)
        
        return highPrice