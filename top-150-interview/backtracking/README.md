# Backtracking Index

此索引整理 `top-150-interview/backtracking` 的題目，並提供回溯法通用模板與複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 017. Letter Combinations of a Phone Number | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [017. Letter Combinations of a Phone Number](./17.%20Letter%20Combinations%20of%20a%20Phone%20Number.md) |
| 046. Permutations | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [046. Permutations](./46.%20Permutations.md) |
| 077. Combinations | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [077. Combinations](./77.%20Combinations.md) |

## 回溯法通用模板 (Backtracking Pattern)

回溯法（Backtracking）本質上是一種**深度優先搜尋（DFS）**，透過建立一棵決策樹來遍歷所有可能的解。其核心模式為「**做選擇 $\rightarrow$ 遞迴探索 $\rightarrow$ 撤銷選擇（狀態復原）**」。

### Java 標準程式碼模板

```java
void backtrack(元素列表 nums, 狀態/標記, List<Integer> current, List<List<Integer>> result) {
    // 1. 遞迴終止條件 (Base Case)
    if (滿足終止條件) {
        // 複製當前路徑並存入結果（避免後續修改影響）
        result.add(new ArrayList<>(current));
        return;
    }

    // 2. 遍歷當前層級的所有候選選擇
    for (int i = startIndex; i < nums.length; i++) {
        // 剪枝條件 / 排除無效解
        if (不符合條件) {
            continue;
        }

        // 3. 做選擇
        current.add(nums[i]);
        used[i] = true; // （若為排列題）

        // 4. 進入下一層遞迴
        backtrack(nums, ..., current, result);

        // 5. 撤銷選擇 (Backtrack / 狀態復原)
        current.remove(current.size() - 1);
        used[i] = false; // （若為排列題）
    }
}
```

---

## 常見題型與策略

| 題型類別 | 特徵與應用場景 | 遍歷/剪枝策略 | 代表題目 |
| --- | --- | --- | --- |
| **組合 (Combinations)** | 順序無關（`[1,2]` 與 `[2,1]` 視為相同） | 使用 `startIndex` 控制下一層搜尋範圍，避免選到前面的元素。 | 77, 17 |
| **排列 (Permutations)** | 順序相關（`[1,2]` 與 `[2,1]` 視為不同） | 每次從 `0` 開始遍歷，使用 `used[]` 陣列記錄哪些元素已被使用。 | 46 |
| **子集 (Subsets)** | 找尋決策樹上的每一個節點 | 每個節點都是一個合法答案，在遞迴開頭直接收集 `current`。 | 78, 90 |
| **去重剪枝 (Duplicates)** | 輸入含有重複元素，要求輸出不能重複 | 先排序 `Arrays.sort(nums)`，若 `i > startIndex && nums[i] == nums[i-1]` 則 `continue`。 | 40, 90 |

---

## 關鍵實作細節與注意事項

1. **路徑複製 (Deep Copy)**：
   在將 `current` 加入 `result` 時，必須使用 `new ArrayList<>(current)` 建立副本。若直接傳入 `current`，後續回溯的 `remove` 操作會將結果集中的內容一併修改。

2. **選擇與撤銷成對出現**：
   `add` 與 `remove`（以及 `used[i] = true` 與 `used[i] = false`）必須嚴格成對出現，且分別位於遞迴調用的前後。

3. **複雜度評估**：
   - 組合問題：$O(C(n, k))$ 或 $O(2^n)$
   - 排列問題：$O(n!)$
   - 空間複雜度主要取決於遞迴堆疊深度 $O(n)$ 與暫存路徑。
