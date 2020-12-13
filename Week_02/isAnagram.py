# 有效的字母异位词, 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词
# Python
# 1, 直接判断排序后是否相等
# 2, collections Counter方法
# 3, 利用字典计数

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        # return collections.Counter(s) == collections.Counter(t)
        dic1, dic2 = {}, {}
        for item1 in s:
            dic1[item1] = dic1.get(item1, 0) + 1
        for item2 in t:
            dic2[item2] = dic2.get(item2, 0) + 1
        return dic1 == dic2

testcase1 = Solution('anagram')
testcase2 = Solution('nagaram')

