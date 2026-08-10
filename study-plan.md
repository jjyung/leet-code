# Study Plan for Interview Prep

這份計畫以「提高面試通關機率」為目標，並把完整的 LeetCode Top Interview 150 與目前 repository 裡已完成的題解分開看待。

> 重要：目前 repository 只有部分題解，不能把「已寫過」當成「已複習」。完整範圍以 [LeetCode Top Interview 150](https://leetcode.com/studyplan/top-interview-150/) 為準；每題都要另外標記 `未開始`、`看過`、`能獨立完成` 或 `已熟練`。

## 核心策略

1. 先完成 Top Interview 150 的全範圍盤點，再依弱點安排題目；不要只沿著 repository 已有的資料夾讀。
2. 每題採固定流程：先獨立想 20-30 分鐘 -> 口述 brute force 與最佳解 -> 寫 Java -> 測試邊界 -> 複盤錯因。
3. 複習節奏使用 `當天、隔天、第 3 天、第 7 天、第 14 天`；忘記或無法獨立寫出的題目立即回到下一輪。
4. 每個主題至少掌握：辨識訊號、基本模板、複雜度、兩道代表題、一道變形題。
5. 新題與舊題比例：前期 2:1，中期 1:1，考前 1:2。考前不要用大量新題製造虛假的進度感。
6. 每週至少一次 45-60 分鐘限時 mock；最後 4 週提高到每週 2 次。每次 mock 都要記錄失分原因。

## 必須覆蓋的主題

依面試常見程度與相互依賴性安排，不代表 Top 150 官方分類順序：

1. Array / String / HashMap / HashSet
2. Two Pointers / Sliding Window / Prefix Sum
3. Stack / Monotonic Stack / Queue
4. Binary Search
5. Linked List
6. Binary Tree / BST / Tree BFS
7. Heap / Priority Queue
8. Intervals / Greedy
9. Backtracking / Recursion
10. Graph BFS / DFS / Union-Find / Topological Sort
11. Trie
12. Dynamic Programming：一維、二維、背包、LCS/LIS、股票、區間 DP
13. Bit Manipulation / Math / Matrix

DP 安排在後續集中訓練階段，重點是掌握「重複子問題 + 最佳子結構」的辨識方式，以及 state、transition、base case 與 iteration order。

## 每週固定節奏

- 週一至週四：每天 1 題新題 + 1 題到期複習題。
- 週五：只做本週錯題與一題未看過的 medium，補齊錯誤分類。
- 週六：一次限時 mock，結束後完整重寫最不穩的一題。
- 週日：整理錯題清單、檢查所有主題覆蓋率，安排下週的 DP／弱點複習。
- 每天最後 10 分鐘：不看答案寫出今天題目的題型訊號與解法骨架。

## 1-Year Plan

1. Month 1-3：完成 Top 150 第一輪，按主題覆蓋全部範圍；每週固定加入 DP。
2. Month 4-6：完成 Top 150 第二輪，集中 medium、Binary Search、Heap、Backtracking、Graph 與 DP。
3. Month 7-9：每週 2 次 mock，加入目標公司題目，補做錯誤率最高的主題。
4. Month 10-12：以限時整套、錯題重做、行為題和公司題庫為主，不再盲目擴充題量。
5. 通關門檻：Top 150 至少 120 題能在限時內獨立完成；其餘題目至少能說出核心解法與複雜度；DP、Graph、Tree 不得有完全空白主題。

## 6-Month Plan

1. Month 1：Array/String、HashMap、Two Pointers、Sliding Window、Stack、Binary Search。
2. Month 2：Linked List、Tree、BST、Tree BFS、Heap、Intervals、Greedy。
3. Month 3：Graph BFS/DFS、Union-Find、Topological Sort、Trie、Backtracking。
4. Month 4：DP 集中訓練：一維、二維、背包、LIS/LCS、股票與區間 DP；同步補前面錯題。
5. Month 5：完成 Top 150 第二輪與公司高頻題，每週 2 次 mock。
6. Month 6：限時整合、錯題三刷、行為題與面試環境演練。
7. 目標：Top 150 至少完整過一輪，二輪只保留錯題與不穩題；不要用 repository 題解數量當完成數。

## 3-Month Plan

1. Week 1-2：Array/String、HashMap、Two Pointers、Sliding Window、Prefix Sum。
2. Week 3：Stack、Queue、Binary Search、Linked List。
3. Week 4：Binary Tree、BST、Tree BFS、Heap。
4. Week 5：Graph BFS/DFS、Union-Find、Topological Sort、Trie。
5. Week 6：Intervals、Greedy、Backtracking、Bit Manipulation。
6. Week 7-8：DP 集中週，涵蓋一維／二維、0/1 Knapsack、Unbounded Knapsack、LIS/LCS、股票。
7. Week 9-10：Top 150 未完成題 + 所有錯題二刷，每週 2 次 mock。
8. Week 11-12：混合限時題、公司題、錯題三刷與行為題。
9. 目標：優先完成完整 Top 150；若時間不足，保留每個主題的代表題與錯題，不得整類跳過。

## 1-Month Plan

1. Week 1：Array/String、HashMap、Two Pointers、Sliding Window、Stack、Binary Search。
2. Week 2：Linked List、Tree/BST、Heap、Intervals、Greedy。
3. Week 3：Graph、Union-Find、Topological Sort、Backtracking、Trie、Bit Manipulation。
4. Week 4：DP 為主（至少 8 題代表題）+ 混合 mock + 全部錯題重做。
5. 每天：1 題新題 + 2 題複習題；每 3 天做一次 45 分鐘限時練習。
6. 目標：建立所有主題的最低可用能力；不追求把 150 題全部重新寫成筆記。

## 1-Week Plan

1. Day 1：Array/String、HashMap、Two Pointers、Sliding Window。
2. Day 2：Stack、Queue、Binary Search、Linked List。
3. Day 3：Tree、BST、Tree BFS、Heap。
4. Day 4：Graph BFS/DFS、Union-Find、Topological Sort、Trie。
5. Day 5：Backtracking、Intervals、Greedy、Bit Manipulation。
6. Day 6：DP：一維、二維、0/1 Knapsack、LIS/LCS、股票；至少做 5 題。
7. Day 7：2 場 mock、錯題重做、整理每個主題的一頁模板；晚上停止大量刷題並睡眠。

## 3-Day Plan

1. Day 1：Array/HashMap/Two Pointers/Sliding Window/Stack + 一場 mock。
2. Day 2：Binary Search/Linked List/Tree/Heap/Graph + 一場 mock。
3. Day 3：DP、Backtracking、Intervals/Greedy/Trie + 錯題重做；最後一場 mock 只做最弱主題。
4. 每天至少保留 2-3 小時複習，不要嘗試在三天內完成 30 題新題。

## 24-Hour Plan

1. Hour 1：整理每個主題的辨識訊號與 Java 模板。
2. Hour 2-5：複習 Array/HashMap、Two Pointers、Sliding Window、Stack、Binary Search。
3. Hour 6-8：複習 Linked List、Tree、Heap、Graph。
4. Hour 9-11：專門複習 DP：state、transition、base case、遍歷方向，以及 0/1 與 unbounded knapsack 的差異。
5. Hour 12-15：做一場完整 mock，檢討後重寫錯題。
6. Hour 16-18：複習 Backtracking、Intervals、Greedy、Trie、Bit Manipulation。
7. Hour 19-21：只重做錯題與最不穩的 3 題，不開新坑。
8. Hour 22-24：準備面試環境、行為題、履歷故事，並保留睡眠時間。

## 完成判定與追蹤

每題只有符合以下條件才算「已掌握」：

- 不看答案能在 Easy 15 分鐘、Medium 30 分鐘內寫出可執行解法。
- 能說明暴力解、最佳解、時間與空間複雜度。
- 能自行測試空輸入、單元素、重複值、邊界值與極端尺寸。
- 隔 7 天重做仍能完成；否則回到錯題清單。

每週檢查一次：完整 Top 150 覆蓋率、各主題掌握率、錯題數、mock 通過率，以及 DP／Graph／Tree 是否有空白。任何一項低於目標，就優先調整複習內容，而不是繼續增加新題。
