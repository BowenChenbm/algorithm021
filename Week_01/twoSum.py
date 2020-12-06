# find out two int which their sum is equal to a target value, it there isn't then return NULL
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listlen = len(nums)
        for i in range(listlen):
            for j in range(i+1, listlen):
                if nums[i] + nums[j] == target:
                    return [i, j]    
        return []
