class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        l = 0
        p = 1
        c = 0
        for r in range(len(nums)):
            p *= nums[r]
            while p >= k:
                p //= nums[l]
                l += 1
            c += (r - l + 1)
        return c