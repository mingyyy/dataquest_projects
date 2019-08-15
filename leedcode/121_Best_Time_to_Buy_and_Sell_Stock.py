class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy, sell = prices[0], prices[1]
        for i in range(1, len(prices)-1):
            p = max(sell - buy, 0)
            if sell < prices[i+1]:
                sell = prices[i+1]
                if p < (prices[i+1]-prices[i]) & buy > prices[i]:
                    buy = prices[i]
        return p

