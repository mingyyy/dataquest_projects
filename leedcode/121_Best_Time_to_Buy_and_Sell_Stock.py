def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy, sell = prices[0], prices[1]
        p = max(sell - buy, 0)
        for i in range(1, len(prices)-1):
            if max(prices[i+1:]) - min(prices[i], buy) > p:
                if buy > prices[i]:
                    buy = prices[i]
                sell = max(prices[i+1:])
            p = max(sell - buy, 0)
            # print(i, p, sell, buy)
        return p


if __name__ == "__main__":
    print(maxProfit([3,3,5,0,0,3,1,4]))
    print(maxProfit([2, 1, 2, 1, 0, 1, 2]))
    print(maxProfit([30,20,10,29,12,9,8,15,7]))
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([]))
    print(maxProfit([9]))
    print(maxProfit([8,2]))
    print(maxProfit([1,3]))
    print(maxProfit([1,2,4]))
    print(maxProfit([3,1,2]))
    print(maxProfit([20,1,9,10,2,12]))
    print(maxProfit([1,4,7,2]))
