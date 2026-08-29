# Heap Index

此索引整理 `top-150-interview/heap` 的題目，並提供 Heap、優先佇列與 Top K 題型的複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 215. Kth Largest Element in an Array | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [215. Kth Largest Element in an Array](./215.%20Kth%20Largest%20Element%20in%20an%20Array.md) |
| 373. Find K Pairs with Smallest Sums | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [373. Find K Pairs with Smallest Sums](./373.%20Find%20K%20Pairs%20with%20Smallest%20Sums.md) |

## 解題思路提示

先問「候選集合中，下一個最值得處理的是誰？」若每次只需要取最小或最大候選，Heap 通常比反覆排序更合適：

1. 定義 heap 中每個元素代表的完整候選狀態。
2. 決定使用 min-heap 或 max-heap，讓 `peek/poll` 對應下一個答案。
3. 取出候選後，依問題的不變量產生下一批候選。
4. 若只保留 Top K，控制 heap 大小，避免保存不必要的元素。

## 必要資料結構與演算法

- **PriorityQueue**：Java 的 `PriorityQueue` 預設是 min-heap；要找最大值需自訂 comparator。
- **大小為 K 的 min-heap**：維持目前最大的 K 個元素，最小者在頂端，超過 K 就移除。
- **大小為 K 的 max-heap**：常用來取出 K 個最小候選或依序輸出。
- **複雜度**：每次操作 heap 為 $O(\log k)$；若處理 `n` 個元素且 heap 限制為 `k`，通常為 $O(n\log k)$，空間為 $O(k)$。

## 複習提醒

- 明確寫出 heap 元素的格式，例如 pair 的 `[sum, rowIndex, columnIndex]`，不要只依賴 magic number。
- 對排序陣列產生候選時，確認同一個候選不會重複加入。
- comparator 要處理相等值，並確認加法可能需要 `long`。
- 測試 `k = 1`、`k` 大於候選數量、重複值與空輸入。
