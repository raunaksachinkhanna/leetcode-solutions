class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # count how many times val appears

        original_length = len(nums)

        # remove all val and count them
        while val in nums:
            nums.remove(val)
            k += 1 #while removing iterate k

        return original_length - k  # This is equivalent to len(nums) now
