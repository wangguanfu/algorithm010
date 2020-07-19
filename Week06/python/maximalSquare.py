class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        res = 0  # 记录结果
        # 定义dp数组，每个元素代表当前位置可以达到的最大的正方形的边长
        # 长宽都多补了一行是为了更方便处理边界上的点也防止越界发生
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        # 从 dp 的 [1,1] 位置开始遍历
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # 下面需要将坐标映射回 matrix 中，注意 dp 数组和 matrix 元素对应关系
                if matrix[i - 1][j - 1] == '1':# 只有 1 才有可能构成正方形
                    if dp[i - 1][j - 1] and dp[i - 1][j] and dp[i][j - 1]:
                        # 如果当前点的左、上、左上都为 1， 才有机会构成更大的正方形
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    else:
                        # 否则说明当前点的左、上、左上不全为1，也就是有0
                        # 那么当前节点构成的最大正方形就是自身构成的边长为 1 的正方形
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
        return pow(res, 2)
