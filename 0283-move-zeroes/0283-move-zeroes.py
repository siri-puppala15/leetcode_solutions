class Solution(object):
    def moveZeroes(self, nums):
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                if i!=l:
                    nums[l] = nums[i]
                    nums[i]=0
                l+=1
        return nums