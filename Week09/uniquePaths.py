# ：动态规划
#
# 我们令 dp[i][j] 是到达 i, j 最多路径
#
# 动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
#
# 注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1
#
# 时间复杂度：O(m*n)O(m∗n)
#
# 空间复杂度：O(m * n)O(m∗n)
#
# 优化：因为我们每次只需要 dp[i-1][j],dp[i][j-1]
#
# 所以我们只要记录这两个数，直接看代码吧！


# 思路二：
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        #print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]



# 优化1：空间复杂度 O(2n)O(2n)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]


# 优化2：空间复杂度 O(n)O(n)



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

