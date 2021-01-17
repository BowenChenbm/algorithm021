# 127. 单词接龙
# 双向广度优先
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set: return 0
        if beginWord in word_set: word_set.remove(beginWord)

        visited, front_visited, end_visited = set(), set(), set()
        visited.add(beginWord)
        visited.add(endWord)

        front_visited.add(beginWord)
        end_visited.add(endWord)

        word_len = len(beginWord)
        step = 1
        while front_visited:
            if len(front_visited) > len(end_visited): # 取小的进行下面的 while 方便编码
                front_visited, end_visited = end_visited, front_visited
            next_visited = set()
            for word in front_visited:
                temp_word = list(word)
                for j in range(word_len):
                    original_char = temp_word[j]
                    for k in range(26):
                        temp_word[j] = chr(ord('a') + k)
                        nextone = ''.join(temp_word)
                        if nextone in word_set:
                            if nextone in end_visited:
                                return step + 1  #碰到另一端有访问过就找到了，直接return step +1
                            if nextone not in visited:
                                next_visited.add(nextone)
                    temp_word[j] = original_char
            front_visited = next_visited
            step += 1
        return 0


