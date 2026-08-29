# Graph BFS Index

此索引整理 `top-150-interview/graph-bfs` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 433. Minimum Genetic Mutation | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [433. Minimum Genetic Mutation](./433.%20Minimum%20Genetic%20Mutation.md) |
| 909. Snakes and Ladders | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [909. Snakes and Ladders](./909.%20Snakes%20and%20Ladders.md) |

## 解題思路提示

圖的 BFS 適合「每一步成本相同，求最少步數」或「逐層擴散」的問題：

1. 將每個狀態視為節點，將一次合法操作視為一條邊。
2. 起點距離設為 0，入隊後逐層展開所有鄰居。
3. 節點第一次被走訪時，BFS 已用最少步數抵達，因此要立刻標記 visited。
4. 若棋盤座標有特殊映射，先獨立寫出編號到 `(row, column)` 的轉換，再接 BFS。

## 必要資料結構與演算法

- **Queue**：保存待處理狀態；每輪可用層數或 distance 欄位表示步數。
- **visited/距離陣列**：避免循環與重複入隊，狀態數為 `V` 時空間為 $O(V)$。
- **Adjacency generation**：若圖不需完整建立，可在取出節點時即時計算鄰居。
- **複雜度**：顯式圖通常為 $O(V + E)$；若每個狀態有固定 `d` 個操作，則約為 $O(Vd)$。

## 複習提醒

- visited 應在入隊時標記，而不是出隊時，否則同一狀態可能重複排隊。
- 最短步數的起點距離是 0；確認題目問的是邊數、操作次數或層數。
- 棋盤、基因字串等隱式圖要檢查每個生成狀態是否合法。
- 測試起點就是終點、無法抵達、存在循環與多條同長度路徑。
