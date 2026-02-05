class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        oldPrice = prices[0]
        profit = 0 - oldPrice
        bought = True
        
        for day in range(len(prices)):
            price = prices[day]
            if bought:
                if price <= oldPrice:
                    profit = profit + oldPrice
                    oldPrice = prices[day]
                    profit = profit - oldPrice
                else:
                    bought = False
                    oldPrice = prices[day]
                    profit = profit + oldPrice
            else:
                if price >= oldPrice:
                    profit = profit - oldPrice
                    oldPrice = prices[day]
                    profit = profit + oldPrice
                else:
                    bought = True
                    oldPrice = prices[day]
                    profit = profit - oldPrice
        
        if bought:
            profit = profit + oldPrice
        
        return profit if profit > 0 else 0