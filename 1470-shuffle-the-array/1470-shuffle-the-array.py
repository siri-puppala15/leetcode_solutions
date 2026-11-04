class Solution(object):
    def shuffle(self, nums, n):
        max_val = 1001
        for i in range(n - 1, -1, -1):
            nums[2 * i + 1] += (nums[n + i] % max_val) * max_val
            nums[2 * i] += (nums[i] % max_val) * max_val
        for i in range(2 * n):
            nums[i] = nums[i] // max_val
        return nums