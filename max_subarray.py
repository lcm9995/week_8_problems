class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums[:]
        for i in range(1, len(nums)):
            arr[i]= max(nums[i], nums[i]+arr[i-1])
        return max(arr)