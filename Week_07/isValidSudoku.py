# 36. 有效的数独
# 遍历一遍，根据数学计算index之间的关系，并存每个数字在行，列和block里出现的次数，发现重复就不符合
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    box[box_index][num] = box[box_index].get(num, 0) + 1
                    if rows[i][num] > 1 or col[j][num] > 1 or box[box_index][num] > 1:
                        return False
        return True
