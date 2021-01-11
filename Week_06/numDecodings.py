# 91. 解码方法
# 一条包含字母 A-Z 的消息通过数字1~26 进行编码，要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数。
# 分清楚边界问题，就能分清DP方程
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        lenght = len(s)
        dp = [1] * (lenght + 1) #dp[0]为哨兵
        for i in range(2, lenght + 1):
            if s[i-1] == '0' and s[i-2] not in '12': return 0
            elif s[i-1] == '0' and s[i-2] in '12':
                dp[i] = dp[i-2]
            elif '10' < s[i-2:i] <= '26':
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[lenght]
