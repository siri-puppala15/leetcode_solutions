class Solution(object):
    def maxProfit(self, prices):
        s = prices[0]
        t = 0
        for p in prices:
            if p < s:
                s = p
            elif p - s > t:
                t = p - s
        return t