# Matrix Index

此索引整理 `top-150-interview/matrix` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 036. Valid Sudoku | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [036. Valid Sudoku](./036.%20Valid%20Sudoku.md) |
| 048. Rotate Image | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [048. Rotate Image](./048.%20Rotate%20Image.md) |
| 54. Spiral Matrix | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [54. Spiral Matrix](./54.%20Spiral%20Matrix.md) |

## 解題思路提示

矩陣題先確認座標系統與邊界，再選擇走訪方式：

1. 將每格視為 `(row, column)`，移動前檢查 `0 <= row < rows`、`0 <= column < columns`。
2. 旋轉或轉置題先找座標變換，確認變換後每個元素只被處理一次。
3. 螺旋、邊界收縮題用 `top/bottom/left/right` 代表尚未處理的矩形。
4. 格子之間有連通關係時，把它視為圖，使用 DFS/BFS 或 visited 標記。

## 必要資料結構與演算法

- **二維陣列**：用 `matrix[row][column]` 存取；尺寸為 `m x n` 時，完整掃描是 $O(mn)$。
- **方向陣列**：用 `int[][] directions` 統一表示上、下、左、右，減少邊界判斷重複。
- **轉置與反轉**：順時針旋轉正方形矩陣可拆成 transpose + reverse each row。
- **visited 或原地標記**：連通區域題需避免重複走訪；若能修改輸入，可省下 $O(mn)$ 空間。

## 複習提醒

- 先分清楚 `rows` 與 `columns`，不要假設所有矩陣都是正方形。
- 螺旋走訪每次改變邊界後，要確認單列或單欄不會被重複處理。
- 旋轉題用 2 x 2 或 3 x 3 畫圖驗證座標方向，再實作交換。
- Sudoku 類題要分別維護列、欄、區塊的限制，不能只檢查整張矩陣。
