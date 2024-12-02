class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) & 1:
            return False
        bit_cache = 1
        for n in nums:
            bit_cache |= bit_cache << n
        return bool(bit_cache & (1 << int(sum(nums) / 2)))