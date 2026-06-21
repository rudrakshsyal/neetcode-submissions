# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                     profit = max(profit, prices[j] - prices[i])
#         return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
