class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1
        i=0
        for j in range(len(nums)):
            if target < nums[j]:
                return i
            i+=1
        return i