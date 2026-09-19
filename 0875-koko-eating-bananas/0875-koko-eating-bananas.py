class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2
            a=0
            for p in piles:
                a += (p+mid-1)//mid
            if a<=h:
                high = mid
            else:
                low=mid+1
        return low