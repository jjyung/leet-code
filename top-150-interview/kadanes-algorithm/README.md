# Kadane's Algorithm Index

此索引整理 `top-150-interview/kadanes-algorithm` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 053. Maximum Subarray | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [053. Maximum Subarray](./053.%20Maximum%20Subarray.md) |
| 918. Maximum Sum Circular Subarray | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [918. Maximum Sum Circular Subarray](./918.%20Maximum%20Sum%20Circular%20Subarray.md) |

## 解題思路提示

Kadane's Algorithm 將「以目前位置結尾的最佳連續子陣列」當成狀態：

1. 對每個元素選擇「從目前元素重新開始」或「接在前一段後面」。
2. 每一步更新局部最佳值，再更新全域最大值。
3. 循環陣列要分成兩種情況：答案不跨邊界，或答案跨邊界。
4. 跨邊界的最大和可轉成「總和減去中間最小子陣列」，但必須排除整個陣列都被取走的非法情況。

## 必要資料結構與演算法

- **局部狀態**：`current` 表示以目前元素結尾的最大和，不需要保存整個 DP 陣列。
- **全域狀態**：`best` 保存掃描至今的最大答案；循環題另維護最小子陣列和。
- **Kadane 轉移**：`current = max(value, current + value)`，每個元素只處理一次。
- **複雜度**：時間為 $O(n)$、額外空間為 $O(1)$；`n` 是陣列長度。

## 複習提醒

- 全是負數時不能把答案初始化為 0，否則會錯把空子陣列當答案。
- Circular Subarray 要檢查 `total == minSubarray`，避免回傳空集合的結果。
- 分清楚「連續」與「可任意選取」；Kadane 不適用於任意子序列。
- 用單一元素、全負數、全正數、最大值跨首尾與最大值不跨首尾測試。
