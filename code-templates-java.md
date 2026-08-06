# Code templates (Java)

> 依 LeetCode Cheatsheets 常用題型整理，作為刷題時可直接複製的模板集合。

## 0) Base skeleton

```java
class Solution {
    public int solve(int[] nums) {
        // TODO
        return 0;
    }
}
```

## 1) Two pointers: one input, opposite ends

```java
class Solution {
    public int fn(int[] arr) {
        int left = 0, right = arr.length - 1;
        int ans = 0;

        while (left < right) {
            // 依題意更新 ans
            ans = Math.max(ans, arr[left] + arr[right]);

            // 移動左指標的條件
            if (arr[left] < arr[right]) {
                left++;
            } else {
                right--;
            }
        }

        return ans;
    }
}
```

## 2) Two pointers: two inputs, exhaust both

```java
class Solution {
    public int fn(int[] arr1, int[] arr2) {
        int i = 0, j = 0;
        int ans = 0;

        while (i < arr1.length && j < arr2.length) {
            // 依題意處理當前元素
            if (arr1[i] < arr2[j]) {
                ans += arr1[i];
                i++;
            } else {
                ans += arr2[j];
                j++;
            }
        }

        // 耗盡剩餘元素
        while (i < arr1.length) {
            ans += arr1[i++];
        }
        while (j < arr2.length) {
            ans += arr2[j++];
        }

        return ans;
    }
}
```

## 3) Sliding window

```java
class Solution {
    public int fn(int[] arr) {
        int left = 0;
        int curr = 0; // 當前視窗的統計值（如 sum、count）
        int ans = 0;

        for (int right = 0; right < arr.length; right++) {
            // 將 arr[right] 加入視窗
            curr += arr[right];

            // 當視窗違反條件時，從左側縮小
            while (curr > 10) { /* 違反條件 */
                curr -= arr[left];
                left++;
            }

            // 更新答案（此時視窗 [left, right] 合法）
            ans = Math.max(ans, right - left + 1);
        }

        return ans;
    }
}
```

## 4) Build a prefix sum

```java
class Solution {
    public int[] fn(int[] arr) {
        int[] prefix = new int[arr.length + 1]; // prefix[0] = 0，方便計算任意區間和
        for (int i = 0; i < arr.length; i++) {
            prefix[i + 1] = prefix[i] + arr[i];
        }
        // 區間 [l, r] 的和 = prefix[r+1] - prefix[l]
        return prefix;
    }
}
```

## 5) Efficient string building

```java
class Solution {
    public String fn(String[] words) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            sb.append(word);
            sb.append(" ");
        }
        // trim 去除尾端空白
        return sb.toString().trim();
    }
}
```

## 6) Linked list: fast and slow pointer

```java
class Solution {
    public ListNode fn(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;       // 慢指標走一步
            fast = fast.next.next;  // 快指標走兩步
        }

        // slow 停在中間節點
        return slow;
    }
}
```

## 7) Reversing a linked list

```java
class Solution {
    public ListNode fn(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next; // 暫存下一節點
            curr.next = prev;          // 反轉指標
            prev = curr;
            curr = next;
        }

        return prev; // 新的頭節點
    }
}
```

## 8) Monotonic increasing stack

```java
class Solution {
    public int[] fn(int[] arr) {
        Deque<Integer> stack = new ArrayDeque<>(); // 存 index，值單調遞增
        int[] ans = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            // 當棧頂元素 >= 當前值時彈出（維持遞增）
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                int idx = stack.pop();
                // 對彈出的 idx 做處理（例如記錄 next smaller element）
                ans[idx] = i;
            }
            stack.push(i);
        }

        return ans;
    }
}
```

## 9) Binary tree: DFS (recursive)

```java
class Solution {
    public int dfs(TreeNode node) {
        if (node == null) return 0; // base case

        int left = dfs(node.left);   // 遞迴左子樹
        int right = dfs(node.right); // 遞迴右子樹

        // 後序處理：利用左右子樹結果更新答案
        return 1 + Math.max(left, right); // 範例：樹高
    }
}
```

## 10) Binary tree: DFS (iterative)

```java
class Solution {
    public int dfs(TreeNode root) {
        if (root == null) return 0;

        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        int ans = 0;

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            // 前序處理當前節點
            ans = Math.max(ans, node.val);

            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }

        return ans;
    }
}
```

## 11) Binary tree: BFS

```java
class Solution {
    public int bfs(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int ans = 0;

        while (!queue.isEmpty()) {
            int size = queue.size(); // 當層節點數
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                // 處理當前節點
                ans = Math.max(ans, node.val);

                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            ans++; // 範例：層數計數
        }

        return ans;
    }
}
```

## 12) Graph: DFS (recursive)

> 假設節點編號 0 ~ n-1，graph 為鄰接表。若輸入格式不同，需先轉換。

```java
class Solution {
    boolean[] seen;
    List<List<Integer>> graph;

    public int fn(int[][] edges, int n) {
        graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]); // 無向圖
        }

        seen = new boolean[n];
        return dfs(0);
    }

    private int dfs(int node) {
        int ans = 0;
        for (int neighbor : graph.get(node)) {
            if (!seen[neighbor]) {
                seen[neighbor] = true; // 標記已訪問，避免重複
                ans += dfs(neighbor);
            }
        }
        return ans + 1;
    }
}
```

## 13) Graph: DFS (iterative)

```java
class Solution {
    public int fn(List<List<Integer>> graph, int start, int n) {
        boolean[] seen = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        seen[start] = true;
        int ans = 0;

        while (!stack.isEmpty()) {
            int node = stack.pop();
            // 處理當前節點
            ans++;

            for (int neighbor : graph.get(node)) {
                if (!seen[neighbor]) {
                    seen[neighbor] = true;
                    stack.push(neighbor);
                }
            }
        }

        return ans;
    }
}
```

## 14) Graph: BFS

```java
class Solution {
    public int fn(List<List<Integer>> graph, int start, int n) {
        boolean[] seen = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        seen[start] = true;
        int ans = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            // 處理當前節點
            ans++;

            for (int neighbor : graph.get(node)) {
                if (!seen[neighbor]) {
                    seen[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }

        return ans;
    }
}
```

## 15) Find top k elements with heap

```java
class Solution {
    public int[] fn(int[] arr, int k) {
        // 最小堆：保留最大的 k 個元素
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int num : arr) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll(); // 彈出最小值，堆中始終保留最大 k 個
            }
        }

        int[] ans = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            ans[i] = minHeap.poll();
        }
        return ans;
    }
}
```

## 16) Binary search

```java
class Solution {
    public int fn(int[] arr, int target) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; // 防止 overflow
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1; // 未找到
    }
}
```

## 17) Binary search: duplicate elements, left-most insertion point

```java
class Solution {
    public int fn(int[] arr, int target) {
        int left = 0, right = arr.length;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid; // 持續往左逼近
            }
        }

        return left; // 第一個 >= target 的位置
    }
}
```

## 18) Binary search: duplicate elements, right-most insertion point

```java
class Solution {
    public int fn(int[] arr, int target) {
        int left = 0, right = arr.length;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] <= target) {
                left = mid + 1; // 持續往右逼近
            } else {
                right = mid;
            }
        }

        return left; // 最後一個 <= target 的位置 + 1
    }
}
```

## 19) Binary search: for greedy problems

```java
class Solution {
    public int fn(int[] arr) {
        int left = /* 答案下界 */ 1;
        int right = /* 答案上界 */ 1_000_000;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid, arr)) {
                right = mid - 1; // mid 可行，嘗試更小
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    // 判斷 mid 是否滿足貪心條件
    private boolean check(int mid, int[] arr) {
        // TODO: 依題意實作
        return true;
    }
}
```

## 20) Backtracking

```java
class Solution {
    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> fn(int[] nums) {
        backtrack(nums, 0, new ArrayList<>());
        return ans;
    }

    private void backtrack(int[] nums, int start, List<Integer> curr) {
        // 達到終止條件時記錄答案
        ans.add(new ArrayList<>(curr));

        for (int i = start; i < nums.length; i++) {
            curr.add(nums[i]);            // 選擇
            backtrack(nums, i + 1, curr); // 遞迴
            curr.remove(curr.size() - 1); // 撤銷選擇（回溯）
        }
    }
}
```

## 21) Dynamic programming: top-down memoization

```java
class Solution {
    Map<Integer, Integer> memo = new HashMap<>();

    public int fn(int[] arr) {
        return dp(arr, 0);
    }

    private int dp(int[] arr, int i) {
        if (i >= arr.length) return 0; // base case
        if (memo.containsKey(i)) return memo.get(i); // 已計算則直接返回

        int ans = Math.max(
            dp(arr, i + 1),           // 不選 arr[i]
            arr[i] + dp(arr, i + 2)   // 選 arr[i]（依題意決定跳幾步）
        );

        memo.put(i, ans);
        return ans;
    }
}
```

> **Bottom-up 轉換步驟：**
> 1. 依狀態變數大小初始化 `dp[]` 陣列
> 2. 設定 base case（通常初始化為 0）
> 3. 從 base case 往答案方向迭代（注意方向）
> 4. 將 `dp(...)` 呼叫改寫為 `dp[...]` 存取
> 5. 回傳 `dp[目標狀態]`

```java
class Solution {
    public int fnBottomUp(int[] arr) {
        int n = arr.length;
        int[] dp = new int[n + 2]; // 多開兩格避免 index 越界

        for (int i = n - 1; i >= 0; i--) {
            dp[i] = Math.max(dp[i + 1], arr[i] + dp[i + 2]);
        }

        return dp[0];
    }
}
```

## 22) Build a trie

```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false; // 標記單詞結尾
}

class Trie {
    TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return false;
            node = node.children[idx];
        }
        return node.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return false;
            node = node.children[idx];
        }
        return true;
    }
}
```

## 23) Dijkstra's algorithm

```java
class Solution {
    public int[] fn(int[][] edges, int n, int src) {
        // 建立鄰接表：graph.get(u) = [(v, weight), ...]
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        // 最小堆：[距離, 節點]
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, src});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], node = curr[1];

            if (d > dist[node]) continue; // 已有更短路徑，跳過

            for (int[] neighbor : graph.get(node)) {
                int next = neighbor[0], weight = neighbor[1];
                int newDist = dist[node] + weight;
                if (newDist < dist[next]) {
                    dist[next] = newDist;
                    pq.offer(new int[]{newDist, next});
                }
            }
        }

        return dist; // dist[i] 為 src 到節點 i 的最短距離
    }
}
```

ref:
https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/