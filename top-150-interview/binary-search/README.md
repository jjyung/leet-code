# Binary Search Index

此索引整理 `top-150-interview/binary-search` 的題目，並提供二分搜尋的判斷框架與邊界複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 035. Search Insert Position | <span style="color: #16a34a;"><strong>Easy</strong></span> | [035. Search Insert Position](./35.%20Search%20Insert%20Position.md) |
| 074. Search a 2D Matrix | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [074. Search a 2D Matrix](./74.%20Search%20a%202D%20Matrix.md) |

## 解題思路提示

先問：「答案或搜尋空間是否具有單調性？」若每次比較都能排除一半候選，就使用二分搜尋：

1. 定義搜尋區間是閉區間 `[left, right]` 還是半開區間 `[left, right)`。
2. 設定 `mid`，比較後明確排除哪一側。
3. 迴圈結束時，確認要回傳的是找到的位置、`left` 插入點，還是最後可行答案。
4. 矩陣題可先把二維座標映射成一維索引，或先找列再找欄。

## 必要資料結構與演算法

- **有序陣列**：二分搜尋的基本前提；每次將候選範圍縮半。
- **Lower bound**：尋找第一個大於等於目標的位置，常用於插入位置與答案邊界。
- **答案二分搜尋**：當答案範圍可判斷「可行/不可行」且具單調性時，直接對答案值二分。
- **複雜度**：陣列搜尋通常為 $O(\log n)$ 時間、$O(1)$ 空間；`n` 是搜尋範圍大小。

## 複習提醒

- `mid = left + (right - left) / 2` 可避免索引相加溢位。
- 選定區間定義後，初始化、迴圈條件和更新方式必須一致。
- 分別測試空區間、單一元素、目標在兩端、目標不存在與全部元素相同。
- 不要因為題目是矩陣就放棄二分；先檢查列與列之間、列內是否整體有序。
