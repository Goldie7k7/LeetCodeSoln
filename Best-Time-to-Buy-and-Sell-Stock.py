1class Solution:
2    def maxProfit(self, prices: list[int]) -> int:
3        min_price = float('inf')
4        max_profit = 0
5        
6        for i in prices:
7            if i < min_price:
8                min_price = i
9            else:
10                current_profit = i - min_price
11                max_profit = max(current_profit, max_profit)
12                
13        return max_profit