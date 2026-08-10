# LeetCode 類似題目 Todo

以下題目依照與 `q1-0.md` 的相似度及建議練習順序排列。

## 練習清單

- [ ] [Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/) — 預算限制與 Greedy
- [ ] [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — 0/1 Knapsack 基礎
- [ ] [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) — Subset Sum / Knapsack
- [ ] [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) — 二維容量的 0/1 Knapsack
- [ ] [879. Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) — 多維 Knapsack
- [ ] [948. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/) — 資源限制下的 Greedy

## 備註

`q1-0.md` 本質上是 0/1 Knapsack 的特殊變形。由於第 `i` 個項目的收益是 `2^i`，收益具有超遞增特性，因此可以從高 index 往低 index 使用 Greedy，而標準 Knapsack 題目通常需要 DP。
