# Graph General Index

此索引整理 `top-150-interview/graph-general` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 130. Surrounded Regions | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [130. Surrounded Regions](./130.%20Surrounded%20Regions.md) |
| 200. Number of Islands | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [200. Number of Islands](./200.%20Number%20of%20Islands.md) |

## 解題思路提示

網格題常是圖論題的另一種表示。先決定邊界連通規則，再選 DFS、BFS 或 Union-Find：

1. 每個格子視為節點，相鄰且符合條件的格子之間有邊。
2. 逐格掃描，遇到尚未處理的陸地/有效狀態就啟動一次搜尋，累計連通分量。
3. 若要判斷是否被邊界包圍，先從邊界出發標記「一定不會被包圍」的區域。
4. 搜尋過程中同步標記 visited，或利用輸入值改寫代表已處理。

## 必要資料結構與演算法

- **DFS/BFS**：探索四方向或八方向連通區域；時間通常為 $O(mn)$。
- **方向陣列**：統一處理鄰居，避免上下左右邏輯分散。
- **Queue/遞迴 stack**：BFS 的 queue 或 DFS 的呼叫堆疊最多保存與網格大小同階的狀態。
- **Union-Find**：若題目是大量合併與連通性查詢，可用 path compression 降低均攤成本。

## 複習提醒

- 先確認是四連通還是八連通，斜角是否算相鄰不能自行假設。
- 邊界搜尋題要完整檢查第一列、最後一列、第一欄與最後一欄，角落不要重複造成問題。
- 原地把 `1` 改成 `0` 或把安全格標記時，確認題目是否允許修改輸入。
- 測試全水、全陸、單列、單欄、孤立區域與邊界相連區域。
