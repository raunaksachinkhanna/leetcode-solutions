class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # let unique be the sorted set of nums
        unique = sorted(set(nums))

        # overwrite nums with unique values
        for x in range(len(unique)):
            nums[x] = unique[x]

        # return the number of unique elements
        return len(unique)