class Solution(object):
    def twoSum(self, nums, target):
        # Loop through each index x in the nums list
        for x in range(len(nums)):
            # For each x, loop through the indices that come after it (y > x)
            for y in range(x + 1, len(nums)):
                # Check if the sum of nums[x] and nums[y] equals the target
                if nums[x] + nums[y] == target:
                    # If a pair is found, return their indices as a list
                    return [x, y]