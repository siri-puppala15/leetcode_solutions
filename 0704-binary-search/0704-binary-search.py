class Solution(object):
    def search(self, nums, target):
        count = 0
        for i in nums:
            count +=1
            if i == target:
                return count-1
        return -1  