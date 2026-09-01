# Divide and Conquer Index

此索引整理 `top-150-interview/divide-and-conquer` 的題目，並提供分治法、合併與遞迴複雜度的複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 108. Convert Sorted Array to Binary Search Tree | <span style="color: #16a34a;"><strong>Easy</strong></span> | [108. Convert Sorted Array to Binary Search Tree](./108.%20Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree.md) |
| 148. Sort List | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [148. Sort List](./148.%20Sort%20List.md) |

## 解題思路提示

分治法通常可拆成三步：**Divide、Conquer、Combine**。

1. 找到能把問題拆成較小且相似子問題的切分點。
2. 遞迴解決左右或多個子問題。
3. 設計合併步驟，將子答案組成完整答案。
4. 確認 base case 足以停止遞迴，並計算每層工作的成本。

## 必要資料結構與演算法

- **遞迴**：表達同型子問題；二元樹建構常以中點作為根。
- **Merge Sort**：對 linked list 可用快慢指標找中點，再合併兩條已排序串列。
- **區間與中點**：使用 `left + (right - left) / 2`，避免索引溢位。
- **複雜度**：若每層總工作為 $O(n)$ 且有 $O(\log n)$ 層，通常為 $O(n\log n)$；額外空間要分開計算資料結構與遞迴堆疊。

## 複習提醒

- 不要只記「切一半就是 $O(\log n)$」；還要看每層是否必須掃描或合併全部元素。
- linked list 找中點時要處理斷鏈，否則遞迴可能無法結束。
- 合併兩個已排序序列時，先維持「已處理部分有序」的不變量。
- 測試空輸入、單元素、重複值、奇偶長度與極端不平衡資料。
