class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = max(maxP,(prices[r]-prices[l]))
            else:
                l = r 
            r+=1
        return print(maxP)

sol = Solution()
sol.maxProfit([7,1,5,3,6,4])