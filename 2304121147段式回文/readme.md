#### [1147. 段式回文](https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/)

难度困难146收藏分享切换为英文接收动态反馈

你会得到一个字符串 `text` 。你应该把它分成 `k` 个子字符串 `(subtext1, subtext2，…， subtextk)` ，要求满足:

- `subtexti` 是 **非空** 字符串
- 所有子字符串的连接等于 `text` ( 即`subtext1 + subtext2 + ... + subtextk == text` )
- 对于所有 i 的有效值( 即 `1 <= i <= k` ) ，`subtexti == subtextk - i + 1` 均成立

返回`k`可能最大值。

 

**示例 1：**

```
输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。
```





解答：

递归

前缀、后缀哈希表

