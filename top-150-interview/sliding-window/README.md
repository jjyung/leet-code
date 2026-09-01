# Sliding Window Index

此索引整理 `top-150-interview/sliding-window` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 003. Longest Substring Without Repeating Characters | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [003. Longest Substring Without Repeating Characters](./3.%20Longest%20Substring%20Without%20Repeating%20Characters.md) |
| 209. Minimum Size Subarray Sum | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [209. Minimum Size Subarray Sum](./209.%20Minimum%20Size%20Subarray%20Sum.md) |

## 解題思路提示

滑動視窗適用於連續子陣列或子字串，且視窗條件可以透過加入右端、移除左端逐步維護：

1. 右指標向右擴張，將新元素加入計數、總和或集合。
2. 當視窗違反條件時，持續移動左指標並移除離開的元素。
3. 在條件合法的時機更新最長、最短或計數答案。
4. 先確認條件是否具有單調性；若移除左端不能穩定修復條件，標準視窗可能不適用。

## 必要資料結構與演算法

- **左右指標**：每個元素最多進入與離開視窗一次，核心掃描為 $O(n)$。
- **HashMap/陣列計數**：追蹤字元頻率、最後位置或目前視窗中的種類數。
- **Running sum**：正數陣列的最短總和題可用累加和配合縮小視窗。
- **複雜度**：若每次移動只做 $O(1)$ 更新，時間為 $O(n)$；計數結構空間依字元種類或元素種類而定。

## 複習提醒

- `while` 與 `if` 不同：違反條件時通常要持續縮小到重新合法。
- 更新答案的時機很重要：最短通常在合法後縮小，最長通常在合法時擴張。
- 題目若含負數，總和不再具單調性，需考慮前綴和、Deque 或其他方法。
- 測試空字串、重複字元、視窗剛好等於限制、整個輸入都不合法等案例。
