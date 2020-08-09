class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]







class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second

# 复杂度分析
# # #
# # # 时间复杂度：O(n)O(n)，其中 nn 是数组长度。只需要对数组遍历一次。
# # #
# # # 空间复杂度：O(1)O(1)。使用滚动数组，可以只存储前两间房屋的最高总金额，而不需要存储整个数组的结果，因此空间复杂度是 O(1)O(1)。
# # #
