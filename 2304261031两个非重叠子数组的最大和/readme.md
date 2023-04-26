#### [1031. 两个非重叠子数组的最大和](https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/)

难度中等245

给你一个整数数组 `nums` 和两个整数 `firstLen` 和 `secondLen`，请你找出并返回两个非重叠 **子数组** 中元素的最大和*，*长度分别为 `firstLen` 和 `secondLen` 。

长度为 `firstLen` 的子数组可以出现在长为 `secondLen` 的子数组之前或之后，但二者必须是不重叠的。

子数组是数组的一个 **连续** 部分。

 

**示例 1：**

```
输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。
```

**示例 2：**

```
输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。
```

**示例 3：**

```
输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度
```





解题思路
思路是动态规划
动态维护前i个数中连续firstlen长度数组的和的最大值，记为max1
sum1 sum2为前后两个数组的sum，使用滑动窗口维护
对于从i开始后边的数组的情况，最大值为max1+sum2
找到最大的max1+sum2
上边默认firstlen数组在前边，交换顺序再来一遍

