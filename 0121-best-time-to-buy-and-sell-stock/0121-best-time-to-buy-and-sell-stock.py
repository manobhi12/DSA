class Solution:
    def maxProfit(self, prices) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum buying price
            if price < min_price:
                min_price = price
            
            # Calculate profit if sold today
            profit = price - min_price
            
            # Update maximum profit
            if profit > max_profit:
                max_profit = profit
        
        return max_profit     