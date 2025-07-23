class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            nums.add(target)
            sorted(nums)
            return nums.index(target)