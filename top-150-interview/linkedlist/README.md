# Linked List Index

此索引整理 `top-150-interview/linkedlist` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 002. Add Two Numbers | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [002. Add Two Numbers](./002.%20Add%20Two%20Numbers.md) |
| 021. Merge Two Sorted Lists | <span style="color: #16a34a;"><strong>Easy</strong></span> | [021. Merge Two Sorted Lists](./021.%20Merge%20Two%20Sorted%20Lists.md) |
| 141. Linked List Cycle | <span style="color: #16a34a;"><strong>Easy</strong></span> | [141. Linked List Cycle](./141.%20Linked%20List%20Cycle.md) |

## 解題思路提示

linked list 題先畫出節點與指標，明確知道每個指標的前驅、目前節點與下一個節點：

1. 修改鏈結前先保存 `next`，避免失去尚未處理的串列。
2. 需要統一處理頭節點時使用 dummy node，讓插入、合併與刪除都能套用相同流程。
3. 需要知道長度或中點時，用一次或兩次掃描；需要偵測循環時使用快慢指標。
4. 合併排序串列時維持「dummy 後方已排序」，每次接上較小節點。

## 必要資料結構與演算法

- **Node 與 next 指標**：每個節點只知道下一個節點，不能像陣列一樣直接跳躍。
- **Dummy node**：額外建立虛擬頭，讓空串列、插入頭部和合併操作更簡潔。
- **快慢指標**：slow 一次一步、fast 一次兩步，可找中點或判斷 cycle。
- **複雜度**：一次走訪通常為 $O(n)$ 時間；迭代法額外空間為 $O(1)$，遞迴法需計入 $O(n)$ 堆疊。

## 複習提醒

- 空串列、單節點、兩節點、頭尾被修改與有重複值是基本測試組合。
- 反轉或重接鏈結時，依序檢查 `previous`、`current`、`next` 三個角色。
- 使用快慢指標時確認 fast、`fast.next` 是否都安全，再讀取下一層。
- 題目若要求保留原串列，不能直接改動節點鏈結；先確認限制再選原地策略。
