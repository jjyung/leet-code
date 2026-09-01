# Intervals Index

此索引整理 `top-150-interview/intervals` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 056. Merge Intervals | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [056. Merge Intervals](./056.%20Merge%20Intervals.md) |
| 057. Insert Interval | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [057. Insert Interval](./57.%20Insert%20Interval.md) |
| 228. Summary Ranges | <span style="color: #16a34a;"><strong>Easy</strong></span> | [228. Summary Ranges](./228.%20Summary%20Ranges.md) |

## 解題思路提示

區間題先確認輸入是否已排序、端點是否包含，再將問題分成「在左側」、「重疊中」、「在右側」三種位置：

1. 未排序區間通常先依起點排序，建立從左到右的處理順序。
2. 合併時維持目前區間 `[currentStart, currentEnd]`，若下一段起點不超過結尾就延伸它。
3. 插入區間可先輸出所有完全在左側的區間，再處理重疊段，最後輸出右側區間。
4. Summary Ranges 類題則維持連續範圍的起點，遇到斷點才結算。

## 必要資料結構與演算法

- **排序**：依起點排序後，重疊關係只需與前一個合併區間比較；成本通常為 $O(n\log n)$。
- **線性掃描**：排序完成後每個區間只處理一次，時間為 $O(n)$。
- **結果 `List<int[]>`**：保存合併後區間；若題目允許，可直接修改輸入以降低額外空間。
- **複雜度**：整體通常為 $O(n\log n)$ 時間、$O(n)$ 輸出空間；`n` 是區間數量。

## 複習提醒

- 明確判斷端點相接是否算重疊，例如 `[1, 4]` 與 `[4, 5]`。
- 合併後的結尾要取 `max`，不能直接覆寫成下一段結尾。
- 插入區間時要確保空輸入、插在最前/最後、完全包含與完全不重疊都能輸出。
- 寫完後用數線畫出兩三段區間，驗證分類條件沒有遺漏或重複。
