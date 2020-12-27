第四周学习笔记与学习心得：
学习笔记，本周主要为熟练模板为主：
===============================================
深度优先搜索模板：
递归写法：#Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
-------------------------------------------------------
非递归写法：#Python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
===============================================
广度优先搜索模板：
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
=================================================
贪心算法： 通常贪心算法会使用在由一系列选择组成的问题中，贪心的概念会体现在其每一个基于当时信息所做的选择中。 这里贪心挺有用的https://mp.weixin.qq.com/s/O935TaoHE9Eexwe_vSbRAg：
贪心的本质是选择每一阶段的局部最优，从而达到全局最优。
贪心一般解题步骤分为如下四步：
（1）将问题分解为若干个子问题
（2）找出适合的贪心策略
（3）求解每一个子问题的最优解
（4）将局部最优解堆叠成全局最优解
贪心算法没有套路与模板，而且经常会涉及到别的知识，个人觉得他更多是算法上一种比较高维度的思考方向或者整体的方法，而不是具体的想BFS/DFS/二分那样的问题解决方法。
=======================================================
二分查找模板：
# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
==============================================================
学习心得：
这周学习的模板和贪心算法，内容比较多，感觉就是需要熟练和应用，各种变形的题目还是需要一定的编码功底支撑，才能灵活的套用模板，这方面还需要加强。这周在理解题解或者自己码代码时，特别注意了备注，一边写一边加深了模板各个地方的理解，虽然效率有点慢，但是忽然有种豁然开朗的感觉。在下周考试前还得再回顾一下这个月的知识，求考试飘过哈哈。
