class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r]-prices[l] > 0:
                res += prices[r]-prices[l]
                l = r
            else:
                l += 1
            r += 1
        return res