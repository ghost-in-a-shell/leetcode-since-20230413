#### [1187. 使数组严格递增](https://leetcode.cn/problems/make-array-strictly-increasing/)

难度困难138

给你两个整数数组 `arr1` 和 `arr2`，返回使 `arr1` 严格递增所需要的最小「操作」数（可能为 0）。

每一步「操作」中，你可以分别从 `arr1` 和 `arr2` 中各选出一个索引，分别为 `i` 和 `j`，`0 <= i < arr1.length` 和 `0 <= j < arr2.length`，然后进行赋值运算 `arr1[i] = arr2[j]`。

如果无法让 `arr1` 严格递增，请返回 `-1`。

 

**示例 1：**

```
输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
输出：1
解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
```

**示例 2：**

```
输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
输出：2
解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
```

**示例 3：**

```
输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
输出：-1
解释：无法使 arr1 严格递增。
```







动态规划
假设arr1前i个值经过j次变换后，变成长度为i的递增数组。
动态规划数组dp在dp[i][j]存储此时变换后数组的最大元素的最小值，也就是最后一个元素的大小。之所以这样做是因为：前边的值越小，越有利于后边构造递增数组。在同样的变换次数条件下，最大值最小，说明变换效率高。

对于dp[i][j]，分为两种情况：
1.arr1的第i个元素不进行交换，此时，dp[i][j]由dp[i-1][j]得到。如果arr1[i-1]>dp[i-1][j]，满足不必交换的条件，新的最大值就是arr1[i-1]。反之必须进行交换，否则无法单增。
2.arr1的第i个元素进行交换，此时，dp[i][j]由dp[i-1][j-1]得到。在arr2进行二分查找，找到恰好够大的值进行交换。如果找不到，即index==len(arr2)，说明无法由交换满足条件。如果找到了，和当前dp[i][j]比较，取较小者。

注意到，可能在有些情况下，两种情况都无法达成，说明“arr1前i个值经过j次变换后，变成长度为i的递增数组”这件事不可能！也就是dp[i][j]不存在。在实际的实现中，使用10**9+1这个正常不可能取到的值代表不存在。同时，这个值作为初值，可以在上述取较小者时满足逻辑。

最后，我们要找到最小的j，使得arr1前n个值经过j次变换后，变成长度为n的递增数组。其中n为arr1的长度。也就是说，在i==n时如果dp[i][j]存在，即不等于10**9+1时，返回此时的j。

本题所用的动态规划数组dp存储的信息和更新路径如下图所示，红色的线为遍历顺序：


![image-20230420140258394](C:\Users\wyx0926\AppData\Roaming\Typora\typora-user-images\image-20230420140258394.png)