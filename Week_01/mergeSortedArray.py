# merge two sorted array
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 暴力: 合并后排序nums1[:] = sorted(nums1[:m] + nums2)
# 双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1Copy = nums1[:m]
        nums1[:] = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1Copy[i] < nums2[j]:
                nums1.append(nums1Copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m: nums1[i+j:] = nums1Copy[i:]
        if j < n: nums1[i+j:] = nums2[j:]

