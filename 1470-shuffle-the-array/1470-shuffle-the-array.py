class Solution(object):
    def shuffle(self, nums, n):
        s=nums[:n]
        t = nums[n:]
        res = []
        for i in range(n):
            res.append(s[i])
            res.append(t[i])
        return res