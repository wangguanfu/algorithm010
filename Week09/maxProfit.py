# 本题思路
#
# 其实方法一的思路不是凭空想象的，而是由动态规划的思想演变而来。这里介绍一维动态规划思想。
#
# dp[i]dp[i] 表示前 ii 天的最大利润，因为我们始终要使利润最大化，则：
#
# dp[i] = max(dp[i-1], prices[i]-minprice)
# dp[i]=max(dp[i−1],prices[i]−minprice)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0  # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]
# 复杂度分析
# 时间复杂度：O(n)。
# 空间复杂度：O(n)。
