# plus one
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。你可以假设除了整数 0 之外，这个整数不会以零开头。
class Solutions:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join(str(x) for x in digits)
        num_plusone = str(int(num) + 1)
        num_final = [int(i) for i in num_plusone]
        return [0]*(len(digits) - len(num_final)) + num_final
