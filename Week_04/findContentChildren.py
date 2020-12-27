#455. 分发饼干
# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干, 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值
# 贪心遍历，先满足最小胃口的孩子
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        leng, lens = len(g), len(s)
        g.sort();s.sort()
        i = j = result = 0
        while i < leng and j < lens:
            while j < lens and g[i] > s[j]: #如果 饼干不够胃口就往后挪检查下一个，直到有足够的
                j += 1
            if j < lens: # 饼干够胃口的，就把结果加1，一旦都没有, j > lens 就会遍历完退出
                result += 1
            i += 1 # 有够到胃口的就诺小孩+1，看下一个
            j += 1 # 饼干被分配了，看下一块饼干
        return result
