class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]


# 复杂度分析
#
# 时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是网格的行数和列数。需要对整个网格遍历一次，计算 \textit{dp}dp 的每个元素的值。
#
# 空间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是网格的行数和列数。创建一个二维数组 dpdp，和网格大小相同。
# 空间复杂度可以优化，例如每次只存储上一行的 \textit{dp}dp 值，则可以将空间复杂度优化到 O(n)O(n)
#
