# Code templates (Java)

ref:
https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/

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

## 1) Two pointers (opposite ends)

```java
class Solution {
    public int[] twoSumSorted(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int sum = nums[l] + nums[r];
            if (sum == target) return new int[] {l, r};
            if (sum < target) l++;
            else r--;
        }
        return new int[] {-1, -1};
    }
}
```

## 2) Sliding window (variable size)

```java
class Solution {
    public int longestNoRepeat(String s) {
        int[] cnt = new int[128];
        int left = 0, ans = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            cnt[c]++;
            while (cnt[c] > 1) {
                cnt[s.charAt(left)]--;
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
```

## 3) Sliding window (fixed size k)

```java
class Solution {
    public int maxSumK(int[] nums, int k) {
        int sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        int ans = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            ans = Math.max(ans, sum);
        }
        return ans;
    }
}
```

## 4) Binary search (first true)

```java
class Solution {
    public int firstTrue(int n) {
        int left = 0, right = n; // answer in [0, n]
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isTrue(mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }

    private boolean isTrue(int x) {
        // TODO
        return true;
    }
}
```

## 5) Prefix sum

```java
class Solution {
    public int rangeSum(int[] nums, int l, int r) {
        int[] pref = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        return pref[r + 1] - pref[l];
    }
}
```

## 6) Hash map frequency counting

```java
import java.util.*;

class Solution {
    public Map<Character, Integer> freq(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        return map;
    }
}
```

## 7) Linked list (dummy node)

```java
class ListNode {
    int val;
    ListNode next;
    ListNode(int v) { this.val = v; }
}

class Solution {
    public ListNode removeVal(ListNode head, int target) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;
        while (cur.next != null) {
            if (cur.next.val == target) cur.next = cur.next.next;
            else cur = cur.next;
        }
        return dummy.next;
    }
}
```

## 8) Fast and slow pointers (cycle detect)

```java
class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
```

## 9) Tree DFS (recursive)

```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { this.val = v; }
}

class Solution {
    public void dfs(TreeNode node) {
        if (node == null) return;
        // preorder: node
        dfs(node.left);
        // inorder: node
        dfs(node.right);
        // postorder: node
    }
}
```

## 10) Tree BFS (level order)

```java
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) return ans;

        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.poll();
                level.add(cur.val);
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            ans.add(level);
        }
        return ans;
    }
}
```

## 11) Graph BFS (shortest path in unweighted graph)

```java
import java.util.*;

class Solution {
    public int shortestPath(List<List<Integer>> graph, int src, int dst) {
        int n = graph.size();
        int[] dist = new int[n];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new ArrayDeque<>();
        q.offer(src);
        dist[src] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();
            if (u == dst) return dist[u];
            for (int v : graph.get(u)) {
                if (dist[v] != -1) continue;
                dist[v] = dist[u] + 1;
                q.offer(v);
            }
        }
        return -1;
    }
}
```

## 12) Backtracking

```java
import java.util.*;

class Solution {
    private final List<List<Integer>> ans = new ArrayList<>();
    private final List<Integer> path = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        dfs(0, nums);
        return ans;
    }

    private void dfs(int idx, int[] nums) {
        ans.add(new ArrayList<>(path));
        for (int i = idx; i < nums.length; i++) {
            path.add(nums[i]);
            dfs(i + 1, nums);
            path.remove(path.size() - 1);
        }
    }
}
```

## 13) Dynamic programming (1D)

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}
```

## 14) Monotonic stack (next greater element)

```java
import java.util.*;

class Solution {
    public int[] nextGreater(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Deque<Integer> st = new ArrayDeque<>(); // store indices

        for (int i = 0; i < n; i++) {
            while (!st.isEmpty() && nums[st.peek()] < nums[i]) {
                ans[st.pop()] = nums[i];
            }
            st.push(i);
        }
        return ans;
    }
}
```

## 15) Priority queue (top k)

```java
import java.util.*;

class Solution {
    public int[] topK(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            pq.offer(new int[] {e.getKey(), e.getValue()});
            if (pq.size() > k) pq.poll();
        }

        int[] ans = new int[k];
        for (int i = k - 1; i >= 0; i--) ans[i] = pq.poll()[0];
        return ans;
    }
}
```
