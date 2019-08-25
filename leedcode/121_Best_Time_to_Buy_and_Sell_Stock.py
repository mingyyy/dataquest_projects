def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy, sell, last_p = prices[0], prices[1], 0
        p = max(sell - buy, 0)
        for i in range(1, len(prices)):
            if sell < prices[i]:
                sell = prices[i]
            else:
                if p < prices[i]-buy:
                    sell = prices[i]

            if buy > prices[i] and i != len(prices)-1:
                if p == 0:
                    buy, sell = prices[i], prices[i]
                else:
                    last_p = p
                    buy, sell = prices[i], prices[i]

            p = max(sell - buy, 0)
            # print(i, p, sell, buy)
        return max(p, last_p)


if __name__ == "__main__":
    print(maxProfit([4,11,2,7,1]) - 7)
    print(maxProfit([3,2,7,1,2,3,0,6])-6)
    print(maxProfit([2, 1, 2, 1, 0, 1, 2])-2)
    print(maxProfit([30,20,10])-0)
    print(maxProfit([7,1,5,3,6,4])-5)
    print(maxProfit([])-0)
    print(maxProfit([9])-0)
    print(maxProfit([8,2])-0)
    print(maxProfit([1,3])-2)
    print(maxProfit([1,2,4])-3)
    print(maxProfit([3,1,2])-1)
    print(maxProfit([20,1,9,10,2,12])-11)
    print(maxProfit([1,4,7,2])-6)
    print(maxProfit([11,3,14,7,1,13])-12)