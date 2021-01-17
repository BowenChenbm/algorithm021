学习笔记
这周内容有点多，要记好多东西T_T，中间遇到了不少难理解的地方：
Trie：
在python 的模板中，一开始没理解这里：
for char in word:
    node = node.setdefault(char, {})

尝试把node和root打印出来后，才发现存储的形式为：{'a': {'b': {'s': {'#': True}}}}， 原因是在setdefault返回的是第二个参数的{}，这里刚好是个字典，node接收到这个字典的地址就等于在里面重新开启一个储存位置紧接着检查下一个，直到遇到end_of_word. 中间不存实际单词，每一层key串起来才是我们要的单词。
总结：每个函数或者方法返回的东东，都要看清楚返回的是值还是其他东西。

并查集：
听超哥讲的有点懵，找到了B站这个视频讲的比较好https://www.bilibili.com/video/BV13t411v7Fs?p=1， 更容易理解。

剪枝：本质就是在递归中参加条件，避免重复访问。
双向BFS：已知起点和终点，可以从两端往中间扩散。
启发式搜索A*： piority queue，估价函数，好多很棒（太长）的文章，有空回来再慢慢看。

红黑树和AVL树：
只需要记住概念和重点：
Lookup: AVL > RedBlackTrees
Inter insertion and removal: AVL < RedBlackTrees
store: AVL > RedBlackTrees
AVL used in database where faster retrievals required
