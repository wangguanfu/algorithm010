class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子序列和 = 当前元素自身最大 + 或者 包含之前最大
        :param nums:
        :return:
        """
        #时间复杂对O(n)
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(nums[i], 0)

        return max(dp)