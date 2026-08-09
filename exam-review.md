# LeetCode 考前一遍複習

這份筆記的目標不是背 150 題，而是看到題目時，能快速辨認資料結構、維持的 invariant，以及正確的複雜度。考試開始後請遵守主辦方對全螢幕、切換分頁與查閱資料的規定。

## 1. 先做的事：讀題與分類

1. 先確認輸入限制、是否已排序、是否允許修改輸入、答案可能是否超過 `int`。
2. 說出暴力解，再問自己：哪一段重複計算或重複掃描可以消除？
3. 對照關鍵字分類：
   - 已排序／兩端靠近：Two Pointers、Binary Search
   - 連續子陣列／子字串：Sliding Window、Prefix Sum
   - 出現次數／配對／去重：HashMap、HashSet、頻率陣列
   - 最近一個／括號／單調關係：Stack、Monotonic Stack
   - 最短步數：BFS；所有節點都要走：DFS/BFS
   - 前 `k` 大小、即時極值：Heap / `PriorityQueue`
   - 區間重疊：先依起點排序，再合併或掃描
   - 所有選擇、排列、組合：Backtracking
   - 相同子問題重複出現：Dynamic Programming

寫程式前先明確定義：`left/right` 代表什麼、視窗何時合法、`dp[i]` 的意義、何時標記 visited。

## 2. 複雜度直覺

| `n` 大小 | 通常可接受 |
| --- | --- |
| `n <= 20` | `O(2^n)`、Backtracking |
| `n <= 1,000` | `O(n^2)` |
| `n <= 100,000` | `O(n log n)` 或 `O(n)` |
| `n` 很大 | `O(log n)` 或 `O(1)` |

常用複雜度：HashMap/HashSet 平均查找 `O(1)`；排序 `O(n log n)`；Heap 每次操作 `O(log k)`；Binary Search `O(log n)`；圖通常是 `O(V + E)`。遞迴 DFS 的空間要加上 recursion stack；排序和 auxiliary data structure 也要算入空間。

## 3. Java 必背模板

### Two Pointers

```java
int left = 0, right = nums.length - 1;
while (left < right) {
    // 使用 nums[left]、nums[right] 更新答案
    if (/* 應該增加左端 */) left++;
    else right--;
}
```

已排序陣列找 pair 時，和太小就 `left++`，和太大就 `right--`。`3Sum` 通常先排序、固定 `i`、再用左右指標，並跳過重複值。

### Sliding Window

```java
int left = 0;
for (int right = 0; right < s.length(); right++) {
    // 將 right 加入視窗
    while (/* 視窗不合法 */) {
        // 移除 left
        left++;
    }
    // 此時 [left, right] 合法，更新答案
}
```

每個元素最多進出一次，所以通常是 `O(n)`。若條件是「恰好」或陣列有負數，不能直接套用只靠總和縮窗的模板；要改用頻率、Prefix Sum 或其他方法。

### HashMap / 頻率

```java
Map<Character, Integer> count = new HashMap<>();
for (char c : s.toCharArray()) {
    count.put(c, count.getOrDefault(c, 0) + 1);
}
```

需要「之前是否出現過」時，先查再放；需要「目前總數」時，放入後再更新。雙向映射（例如 Isomorphic Strings、Word Pattern）必須同時維護兩個 Map。

### Prefix Sum

```java
long[] prefix = new long[nums.length + 1];
for (int i = 0; i < nums.length; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
}
// [l, r] 的和：prefix[r + 1] - prefix[l]
```

### Linked List

```java
ListNode prev = null, curr = head;
while (curr != null) {
    ListNode next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
}
return prev;
```

Dummy node 可統一處理刪除 head、合併串列等邊界。快慢指標判 cycle：`fast != null && fast.next != null` 才能走兩步。

### Stack / Queue

```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(x); stack.pop(); stack.peek();

Queue<Integer> queue = new ArrayDeque<>();
queue.offer(x); queue.poll(); queue.peek();
```

BFS 要在每一層開始時保存 `int size = queue.size()`。不要用 `Stack`；`ArrayDeque` 較適合。單調 stack 通常存 index，遇到破壞單調性的元素時 pop，並在 pop 當下結算答案。

### Binary Tree

```java
void dfs(TreeNode node) {
    if (node == null) return;
    dfs(node.left);
    // inorder：左、根、右
    dfs(node.right);
}
```

BST 的 inorder traversal 會得到遞增順序，因此可用來找第 `k` 小、相鄰差值最小。樹的「高度／路徑／子樹答案」通常是後序 DFS：先取得左右子樹結果，再合併。

### Graph DFS / BFS

```java
boolean[] seen = new boolean[n];
Deque<Integer> queue = new ArrayDeque<>();
queue.offer(start);
seen[start] = true;
while (!queue.isEmpty()) {
    int node = queue.poll();
    for (int next : graph.get(node)) {
        if (!seen[next]) {
            seen[next] = true; // 放入 queue/stack 的同時標記
            queue.offer(next);
        }
    }
}
```

無向圖建 adjacency list 時通常加雙向邊；有向圖只加一邊。若要算 connected components，對每個尚未 visited 的節點重新 DFS/BFS。最短無權路徑用 BFS；有權且權重非負才考慮 Dijkstra。

### Binary Search

```java
int left = 0, right = nums.length - 1;
while (left <= right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] == target) return mid;
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
}
return -1;
```

若找「第一個符合條件」，使用半開區間 `[left, right)`，符合時收縮 `right = mid`；最後答案通常是 `left`。也可以對答案本身二分：先定義 `check(mid)`，確認它是否具有單調性。

## 4. 常見題型的核心 invariant

- **Remove duplicates / move zeroes**：`write` 左側永遠是已處理且符合條件的結果。
- **Best time to buy/sell**：維護至今最低買入價與目前最大利潤。
- **Product except self**：先累積左側乘積，再由右側反向累積；避免除法與零值問題。
- **Jump Game**：維護目前可到達的最遠位置；若 `i > farthest` 就失敗。
- **Merge Intervals**：排序後，若下一段起點 `<=` 目前結尾就合併，否則輸出目前段。
- **Gas Station**：總油量不足必失敗；若目前油量小於零，起點跳到下一站並重設目前油量。
- **Top K**：維護大小為 `k` 的 heap；要保留最大的 k 個就用 min-heap。
- **DP**：先寫出狀態定義與轉移，再決定 top-down 或 bottom-up；不要直接憑感覺填表。

## 5. 最容易失分的地方

- 空陣列、單一元素、全相同、全負數、答案不存在。
- `int` overflow：總和、乘積、距離用 `long`；`mid` 用 `left + (right - left) / 2`。
- Java 字串比較用 `.equals()`，不是 `==`。
- `Arrays.asList(int[])` 不會得到 `List<Integer>`；primitive array 需自行轉換。
- `List.remove(0)` 是 `O(n)`；需要 queue 時用 `ArrayDeque`。
- 遞迴前確認 base case；圖 traversal 進入鄰居前標記 visited，避免重複或無限循環。
- 複製答案時要 `new ArrayList<>(current)`，不能直接加入可變動的同一個 list。
- 輸出 `List<List<Integer>>` 時，避免把內部暫存 list 在 backtrack 後直接共用。

## 6. 開始作答前的 60 秒檢查

1. 我能用一句話說明每個指標、Map、stack 或 `dp` 的意義嗎？
2. 我的 while/for 是否一定會前進？是否可能 index 越界？
3. 我是否在正確時機更新答案，而不是漏掉最後一個視窗或最後一個節點？
4. 我是否處理空輸入、重複值、負數、overflow 與不存在的答案？
5. 寫出時間、空間複雜度，並用最小案例手動跑一次。

記住：先求正確，再做最佳化；遇到卡題時，回到「暴力解會重複做什麼？」通常就能找到該維護的狀態。
