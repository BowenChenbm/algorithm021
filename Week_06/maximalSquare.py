# 221. 最大正方形
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] 输出：4
# DP = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1) + 1, 最小边界决定最长能到达位置。dp表示以该位置为右下角的正方形能达到的最大正方形边界
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        if rows == 0 or columns == 0: return 0
        dp = [[0] * columns for _ in range(rows)]
        maximaLength = 0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maximaLength = max(maximaLength, dp[i][j])
        return maximaLength*maximaLength
