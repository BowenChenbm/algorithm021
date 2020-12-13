# 两数之和, two
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍
# Python3
# 1, 枚举
# 2, 哈希表

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

# 1，枚举：
        # listlen = len(nums)
        # for i in range(listlen):
        #     for j in range(i+1, listlen):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

#2, 哈希表，空间换时间基本思想: 在遍历的同时，记录一些信息，以省去一层循环。这里需要记录已经遍历过的数值和它所对应的下标，可使用查找表实现（哈希表和平衡二叉搜索树），因为这里不需要维护查找表的顺序，故使用哈希表即可。
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num not in hashtable:
                hashtable[num] = i
            else:
                return [hashtable[target - num], i]
        return []

       
        
