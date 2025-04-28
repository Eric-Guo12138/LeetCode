class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 遍历prices，买入价选择最小值，最大利润为当前价-买入价的最大值
        buy = prices[0]
        maxprofit = 0
        for price in prices:
            buy = min(buy,price)
            maxprofit = max(maxprofit,price-buy)
        return maxprofit