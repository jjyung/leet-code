# Two Pointers Index

此索引整理 `top-150-interview/two-pointers` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 11. Container With Most Water | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [11. Container With Most Water](./11.%20Container%20With%20Most%20Water.md) |
| 125. Valid Palindrome | <span style="color: #16a34a;"><strong>Easy</strong></span> | [125. Valid Palindrome](./125.%20Valid%20Palindrome.md) |
| 15. 3Sum | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [15. 3Sum](./15.%203Sum.md) |
| 167. Two Sum II - Input Array Is Sorted | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [167. Two Sum II - Input Array Is Sorted](./167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.md) |
| 392. Is Subsequence | <span style="color: #16a34a;"><strong>Easy</strong></span> | [392. Is Subsequence](./392.%20Is%20Subsequence.md) |

## 解題思路提示

雙指標的核心是讓兩個索引各自代表一段有意義的區域，並利用排序、方向或已處理結果排除候選：

1. **相向指標**：從左右兩端開始，依條件移動較不可能形成答案的一側。
2. **同向指標**：一個負責掃描，一個負責維持有效區間，常用於移除重複或原地過濾。
3. **固定一個元素後再用雙指標**：3Sum 等題目先排序，再將剩餘問題降成 Two Sum。
4. 每次移動前確認不變量，例如「指標外側的組合已不可能是更好的答案」。

## 必要資料結構與演算法

- **排序**：先排序可讓移動方向具有單調性，也方便跳過重複值；通常成本為 $O(n\log n)$。
- **相向雙指標**：適合有序陣列、容量最大化與兩端配對，掃描階段為 $O(n)$。
- **快慢指標**：適合原地壓縮陣列與判斷序列關係，額外空間可為 $O(1)$。
- **複雜度**：固定一層再線性掃描通常為 $O(n^2)$；排序後的總成本通常為 $O(n\log n + n^2)$。

## 複習提醒

- 先問「為何可以移動這個指標」；若沒有單調性或排序依據，雙指標可能不成立。
- 3Sum 要同時跳過固定元素與左右指標的重複值，避免重複答案。
- 空陣列、單元素、全相同、沒有配對與答案位於兩端都要測試。
- 注意題目要求的是索引、值、布林值或所有組合，輸出形式會影響去重方式。
