# 874. 模拟行走机器人
""" 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

    -2：向左转 90 度
    -1：向右转 90 度
    1 <= x <= 9：向前移动 x 个单位长度

在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dix = [0, 1, 0, -1] # 存放每个方向前进一步的左边变化，分别为北，东，南，西，对应两个数组下标0~3。
        diy = [1, 0, -1, 0]
        x = y = 0
        current = 0 #存放当前方向
        result = 0
        obstacles_set = set(map(tuple, obstacles)) #把障碍坐标做集合处理，保证不重复，加快查询是否在此集合中，即是否路过障碍
        for item in commands:
            if item == -1:
                current = (current + 1) % 4 # 右转90度， 数学方法，右转一次，对应坐标顺时针加1，只有4个方向（下标）循环可用求余4实现
            elif item == -2:
                current = (current + 3) % 4 # 左转90度， 同理，左转一次，对应坐标顺时针加3
            else:
                for i in range(item):
                    if (x + dix[current], y + diy[current]) not in obstacles_set: # 每次加一步判断是否遇到障碍，遇到跳到一个item
                        x += dix[current]
                        y += diy[current]
                        result = max(result, x*x + y*y) # 没有障碍，计算存放最大值
        return result
