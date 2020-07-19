# 思路:
# 动态规划
#
# dp[i]到字符串第i位置最多解码的个数
#
# 动态方程: dp[i] = dp[i-1] + dp[i - 2]
#
# 注意:这里有很多要考虑的情况
#
# 例如:101,100,所以要考虑有0的情况,直接看代码,注释写在里面了!
#
# 再附上自顶向下的动态规划, 大家可以提供 Java版本吗?
#
# 代码:
# 自底向上



class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        # 考虑第一个字母
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1: return dp[-1]
        # 考虑第二个字母
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            # 当出现连续两个0
            if s[i - 1] + s[i] == "00": return 0
            # 考虑单个字母
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # 考虑两个字母
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
# 自顶向下

# python

import functools
class Solution1:
    @functools.lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        ans = 0
        if len(s) >= 1 and s[0] != '0':
            ans += self.numDecodings(s[1:])
        if len(s) >= 2 and s[0] != '0' and int(s[:2]) <= 26:
            ans += self.numDecodings(s[2:])
        return ans
