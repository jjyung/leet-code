# Backtracking Index

此索引整理 `top-150-interview/backtracking` 的題目，並提供回溯與搜尋空間剪枝的複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 017. Letter Combinations of a Phone Number | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [017. Letter Combinations of a Phone Number](./17.%20Letter%20Combinations%20of%20a%20Phone%20Number.md) |
| 077. Combinations | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [077. Combinations](./77.%20Combinations.md) |

## 解題思路提示

回溯適合處理「列出所有可能」、「選或不選」、「排列、組合、切割」等問題。把每次遞迴看成建立一棵決策樹：

1. 定義目前路徑 `path` 代表什麼，以及答案何時完成。
2. 列出目前層級可選的候選項目。
3. 選一個候選、遞迴深入，返回後撤銷選擇。
4. 需要時用排序、`used`、`startIndex` 或限制條件剪枝。

## 必要資料結構與演算法

- **`List` 路徑**：暫存目前選擇；加入候選後遞迴，返回時移除最後一項。
- **結果集合**：在 base case 複製目前路徑，避免後續撤銷選擇影響已完成答案。
- **`startIndex`**：組合題用它避免重複使用前面元素；排列題通常改用 `used[]`。
- **DFS**：以深度代表已選數量，以分支代表下一個選擇。時間複雜度常與輸出數量相關，不要只寫成 $O(n)$。

## 複習提醒

- 先判斷題目要「組合」還是「排列」：順序是否重要、元素能否重複使用。
- `path` 傳入答案時要建立副本；Java 中常見寫法是 `new ArrayList<>(path)`。
- 回溯的 `remove` 必須和 `add` 成對，並放在遞迴返回後。
- 留意空輸入、無候選項目、重複候選值與結果順序要求。
