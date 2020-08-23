### **树**

前序  根左右

中序  左根右

后序  右左根





1. #### Trie树的基本实现和特性

## 参考链接

- [二叉树的层次遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
- [Tire 树代码模板](https://shimo.im/docs/DP53Y6rOwN8MTCQH)
- [实现 Trie](https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/)





![image-20200724222723288](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200724222723288.png)

![image-20200727205130496](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200727205130496.png)

## 实战题目

- [实现 Trie (前缀树) ](https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description)（亚马逊、微软、谷歌在半年内面试中考过）
- [单词搜索 II ](https://leetcode-cn.com/problems/word-search-ii/)（亚马逊、微软、苹果在半年内面试中考过）





并查集代码模板

```
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 ?
		x = i; i = p[i]; p[x] = root 
	return root
```



## 实战题目

- [朋友圈](https://leetcode-cn.com/problems/friend-circles)（亚马逊、Facebook、字节跳动在半年内面试中考过）
- [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)（近半年内，亚马逊在面试中考查此题达到 361 次）
- [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)（亚马逊、eBay、谷歌在半年内面试中考过）





## 参考链接

- [DFS 代码模板](https://shimo.im/docs/UdY2UUKtliYXmk8t)
- [BFS 代码模板](https://shimo.im/docs/ZBghMEZWix0Lc2jQ)
- [AlphaZero Explained](https://nikcheerla.github.io/deeplearningschool/2018/01/01/AlphaZero-Explained/)
- [棋类复杂度](https://en.wikipedia.org/wiki/Game_complexity)

![image-20200726224318006](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200726224318006.png)



## 本周作业

### 简单

- [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)（阿里巴巴、腾讯、字节跳动在半年内面试常考）

### 中等

- [实现 Trie (前缀树) ](https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description)（亚马逊、微软、谷歌在半年内面试中考过）
- [朋友圈](https://leetcode-cn.com/problems/friend-circles)（亚马逊、Facebook、字节跳动在半年内面试中考过）
- [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)（近半年内，亚马逊在面试中考查此题达到 361 次）
- [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)（亚马逊、eBay、谷歌在半年内面试中考过）
- [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/description/)（亚马逊、苹果、微软在半年内面试中考过）
- [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)（亚马逊、Facebook、字节跳动在半年内面试中考过）
- [单词接龙](https://leetcode-cn.com/problems/word-ladder/)（亚马逊、Facebook、谷歌在半年内面试中考过）
- [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)（谷歌、Twitter、腾讯在半年内面试中考过）

### 困难

- [单词搜索 II ](https://leetcode-cn.com/problems/word-search-ii/)（亚马逊、微软、苹果在半年内面试中考过）
- [N 皇后](https://leetcode-cn.com/problems/n-queens/)（亚马逊、苹果、字节跳动在半年内面试中考过）
- [解数独](https://leetcode-cn.com/problems/sudoku-solver/#/description)（亚马逊、华为、微软在半年内面试中考过）



![image-20200730203955532](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200730203955532.png)



![image-20200730204221700](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200730204221700.png)







![image-20200730204422810](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200730204422810.png)



![image-20200730204904292](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200730204904292.png)



****













## 参考链接

- [布隆过滤器的原理和实现](https://www.cnblogs.com/cpselvis/p/6265825.html)
- [使用布隆过滤器解决缓存击穿、垃圾邮件识别、集合判重](https://blog.csdn.net/tianyaleixiaowu/article/details/74721877)
- [布隆过滤器 Python 代码示例](https://shimo.im/docs/UITYMj1eK88JCJTH)
- [布隆过滤器 Python 实现示例](https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/)
- [高性能布隆过滤器 Python 实现示例](https://github.com/jhgg/pybloof)
- [布隆过滤器 Java 实现示例 1](https://github.com/lovasoa/bloomfilter/blob/master/src/main/java/BloomFilter.java)
- [布隆过滤器 Java 实现示例 2](https://github.com/Baqend/Orestes-Bloomfilter)



![image-20200808151214124](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20200808151214124.png)















