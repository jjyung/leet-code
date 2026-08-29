# Stack Index

此索引整理 `top-150-interview/stack` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 020. Valid Parentheses | <span style="color: #16a34a;"><strong>Easy</strong></span> | [020. Valid Parentheses](./020.%20Valid%20Parentheses.md) |
| 071. Simplify Path | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [071. Simplify Path](./071.%20Simplify%20Path.md) |
| 150. Evaluate Reverse Polish Notation | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [150. Evaluate Reverse Polish Notation](./150.%20Evaluate%20Reverse%20Polish%20Notation.md) |
| 155. Min Stack | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [155. Min Stack](./155.%20Min%20Stack.md) |

## 解題思路提示

當題目要求「最近尚未配對的元素」、「後進先出」或逐步解析巢狀結構時，優先考慮 Stack：

1. 將目前無法立即完成的元素 push 進 stack。
2. 遇到能配對或完成運算的元素時，先檢查 stack top，再 pop。
3. 若需要支援額外查詢，例如目前最小值，為每個狀態同步保存足夠資訊。
4. 解析運算式時，明確區分 operand 與 operator，並遵守 operator 的運算順序。

## 必要資料結構與演算法

- **`Deque`/Stack**：Java 建議使用 `Deque` 的 `push/pop/peek`，避免把 `Stack` 和其他容器混用。
- **單調 Stack**：維持遞增或遞減 top，用於下一個更大/更小元素；每個元素最多 push/pop 一次。
- **雙 Stack**：主 stack 保存值，輔助 stack 保存截至目前的最小值或最大值。
- **複雜度**：典型 stack 題每個元素處理一次，時間為 $O(n)$、額外空間為 $O(n)$。

## 複習提醒

- 括號題要同時檢查 stack 是否為空、種類是否匹配，以及最後是否完全清空。
- RPN 運算的第二個 pop 是左運算元，順序不能寫反；除法與減法尤其要測試。
- 路徑解析要分辨空片段、`.` 與 `..`，並避免 `..` 讓根目錄再往上移。
- 每個操作的時間複雜度要符合題目要求；Min Stack 取最小值不能每次重新掃描。
