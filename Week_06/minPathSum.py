# 64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# dp
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        m = len(dp)
        n = len(dp[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
        return dp[m- 1][n -1]
