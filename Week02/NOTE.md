学习笔记

#### 1. 哈希表、映射、集合的实现与特性

Hash: 哈希    链表法和寻址法

0（1）





Set :   可以哈希 也可以树实现



## 实战题目 / 课后作业

- [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)（亚马逊、Facebook、谷歌在半年内面试中考过）
- [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)（亚马逊在半年内面试中常考）
- [两数之和](https://leetcode-cn.com/problems/two-sum/description/)（亚马逊、字节跳动、谷歌、Facebook、苹果、微软、腾讯在半年内面试中常考）



解题思路
首先要熟悉求两数之和的写法，然后在 N > 2时，采用递归处理，一次减少1。
关键点是:

1. 先对nums排序；
2. 递归处理时的剪枝处理(参考注释)
   这种写法参考了国际站上的文章，我觉得是最好的一种解法了。

代码



```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    	if not nums: return []
   # 先排序，关键！
        nums.sort()     
        ans = set()
        N, target = 3, 0
        self._find_sum(nums, 0, N, target, [], ans)
        return list(ans)

    def _find_sum(self, nums, start, N, target, path, ans):
        # terminator
        if len(nums) < N or N < 2: return
        # process
        if N == 2:
            # 两数求和
            d = set()
            for j in range(start, len(nums)):
                if target - nums[j] in d:
                    ans.add(tuple(path + [target - nums[j], nums[j]]))
                else:
                    d.add(nums[j])
        else:
            for i in range(start, len(nums)):
                # 剪枝1: target比剩余数字能组成的最小值还要小 或 比能组成的最大值还要大，就可以停止循环了
                if target < nums[i] * N or target > nums[-1] * N: break
                # 剪枝2: 去重
                if i > start and nums[i] == nums[i - 1]: continue
                # drill down
                self._find_sum(nums, i + 1, N - 1, target - nums[i], path + 					[nums[i]], ans)
        return
```













#### 2 树、二叉树、二叉搜索树的实现和特性

1.升维

2. 链表特殊的树
3. 树特殊的图

```python
class TreeNode:

​	def __init__(self,val):

​			self.val =val
​			self.left, self.right =None, Node
```



4.树的遍历

​		前序    :  根左右

​		中序    :  左根右

​		后序    :  左根右



###### 3.二叉搜索树 (二叉排序树)

​		中序 遍历  升序 数组

​		查询 插入  时间复杂度o(logn)



###### 4.实战

面试题 基本上都是递归

























