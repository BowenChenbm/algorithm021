# rotate array
#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# First mind: create a new array to save the result then copy back to the origianal one
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        temp = [0] * length
        for i in range(len(nums)):
            temp[(i+k) % length] = nums[i]
        nums[:] = temp[:]
