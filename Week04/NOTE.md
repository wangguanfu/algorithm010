学习笔记

#### DFS 代码模板



```
递归写法
自动检测
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
```



```
非递归写法
自动检测
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
```







#### BFS 代码模板

```
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
```



## 实战题目

- [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description)（字节跳动、亚马逊、微软在半年内面试中考过）
- [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description)
- [括号生成](https://leetcode-cn.com/problems/generate-parentheses/#/description)（字节跳动、亚马逊、Facebook 在半年内面试中考过）
- [在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/#/description)（微软、亚马逊、Facebook 在半年内面试中考过）

## 课后作业

- [单词接龙](https://leetcode-cn.com/problems/word-ladder/description/)（亚马逊在半年内面试常考）
- [单词接龙 II ](https://leetcode-cn.com/problems/word-ladder-ii/description/)（微软、亚马逊、Facebook 在半年内面试中考过）
- [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)（近半年内，亚马逊在面试中考查此题达到 350 次）
- [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/description/)（亚马逊、Facebook 在半年内面试中考过）







#### 贪心的实现、特性及实战题目解析

![image-20200630155023101](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200630155023101.png)



## 参考链接

- [coin change 题目](https://leetcode-cn.com/problems/coin-change/)
- [动态规划定义](https://zh.wikipedia.org/wiki/动态规划)

## 课后作业

- [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/)（亚马逊在半年内面试中考过）
- [买卖股票的最佳时机 II ](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)（亚马逊、字节跳动、微软在半年内面试中考过）
- [分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)（亚马逊在半年内面试中考过）
- [模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/description/)
- [跳跃游戏](https://leetcode-cn.com/problems/jump-game/) （亚马逊、华为、Facebook 在半年内面试中考过）
- [跳跃游戏 II ](https://leetcode-cn.com/problems/jump-game-ii/)（亚马逊、华为、字节跳动在半年内面试中考过）

*********

![image-20200630155147790](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200630155147790.png)

![image-20200630155255549](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200630155255549.png)





#### 二分查找的实现、特性及实战题目解析;

![image-20200630160525771](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200630160525771.png)

## 参考链接

- [二分查找代码模板](https://shimo.im/docs/xvIIfeEzWYEUdBPD/)

  ```
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
  
  ```

  

- [Fast InvSqrt() 扩展阅读](https://www.beyond3d.com/content/articles/8/)

## 实战题目

- [x 的平方根](https://leetcode-cn.com/problems/sqrtx/)（字节跳动、微软、亚马逊在半年内面试中考过）
- [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)（亚马逊在半年内面试中考过）

## 课后作业

- [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)（Facebook、字节跳动、亚马逊在半年内面试常考）
- [搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)（亚马逊、微软、Facebook 在半年内面试中考过）
- [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)（亚马逊、微软、字节跳动在半年内面试中考过）
  - 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
    说明：同学们可以将自己的思路、代码写在学习总结中

### 中等：

- [单词接龙](https://leetcode-cn.com/problems/word-ladder/description/)（亚马逊在半年内面试常考）
- [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)（近半年内，亚马逊在面试中考查此题达到 350 次）
- [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/description/)（亚马逊、Facebook 在半年内面试中考过）
- [跳跃游戏](https://leetcode-cn.com/problems/jump-game/) （亚马逊、华为、Facebook 在半年内面试中考过）
- [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)（Facebook、字节跳动、亚马逊在半年内面试常考）
- [搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)（亚马逊、微软、Facebook 在半年内面试中考过）
- [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)（亚马逊、微软、字节跳动在半年内面试中考过）

### 困难

- [单词接龙 II ](https://leetcode-cn.com/problems/word-ladder-ii/description/)（微软、亚马逊、Facebook 在半年内面试中考过）
- [跳跃游戏 II ](https://leetcode-cn.com/problems/jump-game-ii/)（亚马逊、华为、字节跳动在半年内面试中考过）



