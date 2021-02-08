class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i < j:
                    x = x + 1
        return x