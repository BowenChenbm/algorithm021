#122. 买卖股票的最佳时机 II
#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 思路：遍历数组，把第二天跟当天比较，如果比今天大就买进今天明天卖出prices[i+1] - prices[i],局部最优解能达到最终解，此处可贪心。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        profit = 0
        for i in range(length-1):
            if prices[i+1] > prices[i]:
                temppro = prices[i+1] - prices[i]
                profit += temppro
            else:
                continue
        return profit
