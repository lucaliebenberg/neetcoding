# Input: prices = [10,1,5,6,7,1]

# Output: 6

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxp = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP

