# Graph General Index

此索引整理 `top-150-interview/graph-general` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 130. Surrounded Regions | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [130. Surrounded Regions](./130.%20Surrounded%20Regions.md) |
| 133. Clone Graph | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [133. Clone Graph](./133.%20Clone%20Graph.md) |
| 200. Number of Islands | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [200. Number of Islands](./200.%20Number%20of%20Islands.md) |

## 解題思路提示

遇到圖論題，先把題意轉成「節點」與「邊」；網格題則是圖論的另一種表示法：

1. 判斷圖是有向或無向、邊是否有權重、是否可能不連通。
2. 判斷要找的是可達性、連通分量、最短步數、拓撲順序，還是最小成本。
3. 依邊的性質選 BFS、DFS、Union-Find、拓撲排序或最短路徑演算法。
4. 追蹤 `visited` 或狀態顏色，避免重複走訪與無限循環。
5. 網格題中，每個格子視為節點，相鄰且符合條件的格子之間有邊；逐格掃描，遇到尚未處理的節點就啟動一次搜尋，累計連通分量。
6. 若要判斷是否被邊界包圍，先從邊界出發標記「一定不會被包圍」的區域。

## 必要資料結構與演算法

- **Adjacency List**：稀疏圖的常用表示法，空間為 $O(V + E)$。
- **BFS**：無權圖中從起點求最短邊數，使用 `Queue` 並逐層處理；網格題時間通常為 $O(mn)$。
- **DFS**：探索可達區域、連通分量、環與回溯路徑。
- **Union-Find**：動態合併集合、判斷連通性或無向圖環；搭配 path compression 與 union by size/rank。
- **拓撲排序**：只適用 DAG，可用入度 + queue 或 DFS 後序。
- **方向陣列**：處理網格鄰居時統一四方向或八方向邏輯，避免上下左右分散判斷。

其中 `V` 是節點數，`E` 是邊數。不要把矩陣中的列數、欄數直接當成圖的 `V`，要先確認每個格子是否代表節點。

## 複習提醒

- BFS 的 `visited` 通常在入隊時標記，避免同一節點被重複加入 queue。
- 有向圖的 `visited`、`visiting`、`visited` 三種狀態可用來判斷回邊。
- 不要假設圖一定從 0 或某個單一起點全部可達；必要時逐點啟動搜尋。
- 題目若要求最短「步數」，確認起點距離是 0，並清楚一層代表一次邊移動。
- 網格題先確認是四連通還是八連通，斜角是否算相鄰不能自行假設。
- 邊界搜尋題要完整檢查第一列、最後一列、第一欄與最後一欄，角落不要重複造成問題。
- 原地把 `1` 改成 `0` 或把安全格標記時，確認題目是否允許修改輸入。
- 測試全水、全陸、單列、單欄、孤立區域與邊界相連區域。
