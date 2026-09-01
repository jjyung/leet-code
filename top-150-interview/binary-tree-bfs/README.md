# Binary Tree BFS Index

此索引整理 `top-150-interview/binary-tree-bfs` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 199. Binary Tree Right Side View | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [199. Binary Tree Right Side View](./199.%20Binary%20Tree%20Right%20Side%20View.md) |
| 637. Average of Levels in Binary Tree | <span style="color: #16a34a;"><strong>Easy</strong></span> | [637. Average of Levels in Binary Tree](./637.%20Average%20of%20Levels%20in%20Binary%20Tree.md) |

## 解題思路提示

BFS 題的關鍵是以 queue 保存「下一個要處理的節點」，並用每一輪的 queue 大小分隔樹的層級：

1. 根節點先入隊；每輪先記錄 `levelSize = queue.size()`。
2. 只處理這 `levelSize` 個節點，將其子節點加入下一輪。
3. 需要右側視角時，可保存該層最後取出的節點；需要平均值時累加該層所有值。
4. 若題目要求最短層數或第一個符合條件的節點，BFS 找到時即可停止。

## 必要資料結構與演算法

- **Queue/Deque**：FIFO 保證由上到下、由左到右處理節點。
- **Level-order traversal**：用固定的 `levelSize` 避免下一層節點混入目前層。
- **TreeNode**：每個節點最多加入 queue 一次，完整走訪時間為 $O(n)$。
- **複雜度**：時間為 $O(n)$；queue 額外空間為 $O(w)$，`w` 是樹的最大寬度。

## 複習提醒

- 空樹要直接回傳空結果，不能先對 root 取子節點。
- 一定要在每層開始時固定 `levelSize`，不要用 queue 目前動態大小當迴圈上限。
- 右側視角不一定是每層最右節點「先」處理到的節點，應依實際走訪順序取最後一個。
- 測試只有左鏈、只有右鏈、完整樹與不完整樹。
