# Task 1/150
# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices):
        lowest_price = 99999999999999999999
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if prices[i] - lowest_price > max_profit:
                max_profit = prices[i] - lowest_price

        print(max_profit)

sol = Solution()
sol.maxProfit(prices = [7,1,5,3,6,4])