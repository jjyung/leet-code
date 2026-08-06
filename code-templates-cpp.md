# Code templates (C++)

## 0) Base skeleton

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int solve(vector<int>& nums) {
        // TODO
        return 0;
    }
};
```

## 1) Two pointers: one input, opposite ends

```cpp
class Solution {
public:
    int fn(vector<int>& arr) {
        int left = 0, right = arr.size() - 1;
        int ans = 0;

        while (left < right) {
            // 依題意更新 ans
            ans = max(ans, arr[left] + arr[right]);

            if (arr[left] < arr[right]) { // 移動左指標的條件
                left++;
            } else {
                right--;
            }
        }

        return ans;
    }
};
```

## 2) Two pointers: two inputs, exhaust both

```cpp
class Solution {
public:
    int fn(vector<int>& arr1, vector<int>& arr2) {
        int i = 0, j = 0;
        int ans = 0;

        while (i < arr1.size() && j < arr2.size()) {
            // 依題意處理當前元素
            if (arr1[i] < arr2[j]) {
                ans += arr1[i++];
            } else {
                ans += arr2[j++];
            }
        }

        // 耗盡剩餘元素
        while (i < arr1.size()) ans += arr1[i++];
        while (j < arr2.size()) ans += arr2[j++];

        return ans;
    }
};
```

## 3) Sliding window

```cpp
class Solution {
public:
    int fn(vector<int>& arr) {
        int left = 0;
        int curr = 0; // 當前視窗的統計值（如 sum、count）
        int ans = 0;

        for (int right = 0; right < arr.size(); right++) {
            curr += arr[right]; // 將 arr[right] 加入視窗

            while (curr > 10) { // 違反條件時從左側縮小
                curr -= arr[left++];
            }

            // 此時視窗 [left, right] 合法
            ans = max(ans, right - left + 1);
        }

        return ans;
    }
};
```

## 4) Build a prefix sum

```cpp
class Solution {
public:
    vector<int> fn(vector<int>& arr) {
        int n = arr.size();
        vector<int> prefix(n + 1, 0); // prefix[0] = 0，方便計算任意區間和
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + arr[i];
        }
        // 區間 [l, r] 的和 = prefix[r+1] - prefix[l]
        return prefix;
    }
};
```

## 5) Efficient string building

```cpp
class Solution {
public:
    string fn(vector<string>& words) {
        string result;
        for (const string& word : words) {
            result += word; // string += 比反覆拼接 string 更快
            result += ' ';
        }
        if (!result.empty()) result.pop_back(); // 去除尾端空白
        return result;
    }
};
```

## 6) Linked list: fast and slow pointer

```cpp
class Solution {
public:
    ListNode* fn(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;        // 慢指標走一步
            fast = fast->next->next;  // 快指標走兩步
        }

        // slow 停在中間節點
        return slow;
    }
};
```

## 7) Reversing a linked list

```cpp
class Solution {
public:
    ListNode* fn(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr != nullptr) {
            ListNode* next = curr->next; // 暫存下一節點
            curr->next = prev;           // 反轉指標
            prev = curr;
            curr = next;
        }

        return prev; // 新的頭節點
    }
};
```

## 8) Monotonic increasing stack

```cpp
class Solution {
public:
    vector<int> fn(vector<int>& arr) {
        stack<int> st; // 存 index，值單調遞增
        vector<int> ans(arr.size(), -1);

        for (int i = 0; i < arr.size(); i++) {
            // 當棧頂元素 >= 當前值時彈出（維持遞增）
            while (!st.empty() && arr[st.top()] >= arr[i]) {
                int idx = st.top(); st.pop();
                // 對彈出的 idx 做處理（例如記錄 next smaller element）
                ans[idx] = i;
            }
            st.push(i);
        }

        return ans;
    }
};
```

## 9) Binary tree: DFS (recursive)

```cpp
class Solution {
public:
    int dfs(TreeNode* node) {
        if (node == nullptr) return 0; // base case

        int left = dfs(node->left);   // 遞迴左子樹
        int right = dfs(node->right); // 遞迴右子樹

        // 後序處理：利用左右子樹結果更新答案
        return 1 + max(left, right); // 範例：樹高
    }
};
```

## 10) Binary tree: DFS (iterative)

```cpp
class Solution {
public:
    int dfs(TreeNode* root) {
        if (root == nullptr) return 0;

        stack<TreeNode*> st;
        st.push(root);
        int ans = 0;

        while (!st.empty()) {
            TreeNode* node = st.top(); st.pop();
            // 前序處理當前節點
            ans = max(ans, node->val);

            if (node->left) st.push(node->left);
            if (node->right) st.push(node->right);
        }

        return ans;
    }
};
```

## 11) Binary tree: BFS

```cpp
class Solution {
public:
    int bfs(TreeNode* root) {
        if (root == nullptr) return 0;

        queue<TreeNode*> q;
        q.push(root);
        int ans = 0;

        while (!q.empty()) {
            int size = q.size(); // 當層節點數
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                // 處理當前節點
                ans = max(ans, node->val);

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ans++; // 範例：層數計數
        }

        return ans;
    }
};
```

## 12) Graph: DFS (recursive)

> 假設節點編號 0 ~ n-1，graph 為鄰接表。若輸入格式不同，需先轉換。

```cpp
class Solution {
    vector<vector<int>> graph;
    vector<bool> seen;

    int dfs(int node) {
        int ans = 0;
        for (int neighbor : graph[node]) {
            if (!seen[neighbor]) {
                seen[neighbor] = true; // 標記已訪問，避免重複
                ans += dfs(neighbor);
            }
        }
        return ans + 1;
    }

public:
    int fn(vector<vector<int>>& edges, int n) {
        graph.assign(n, {});
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]); // 無向圖
        }

        seen.assign(n, false);
        seen[0] = true;
        return dfs(0);
    }
};
```

## 13) Graph: DFS (iterative)

```cpp
class Solution {
public:
    int fn(vector<vector<int>>& graph, int start, int n) {
        vector<bool> seen(n, false);
        stack<int> st;
        st.push(start);
        seen[start] = true;
        int ans = 0;

        while (!st.empty()) {
            int node = st.top(); st.pop();
            // 處理當前節點
            ans++;

            for (int neighbor : graph[node]) {
                if (!seen[neighbor]) {
                    seen[neighbor] = true;
                    st.push(neighbor);
                }
            }
        }

        return ans;
    }
};
```

## 14) Graph: BFS

```cpp
class Solution {
public:
    int fn(vector<vector<int>>& graph, int start, int n) {
        vector<bool> seen(n, false);
        queue<int> q;
        q.push(start);
        seen[start] = true;
        int ans = 0;

        while (!q.empty()) {
            int node = q.front(); q.pop();
            // 處理當前節點
            ans++;

            for (int neighbor : graph[node]) {
                if (!seen[neighbor]) {
                    seen[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }

        return ans;
    }
};
```

## 15) Find top k elements with heap

```cpp
class Solution {
public:
    vector<int> fn(vector<int>& arr, int k) {
        // 最小堆：保留最大的 k 個元素
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int num : arr) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop(); // 彈出最小值，堆中始終保留最大 k 個
            }
        }

        vector<int> ans(k);
        for (int i = k - 1; i >= 0; i--) {
            ans[i] = minHeap.top(); minHeap.pop();
        }
        return ans;
    }
};
```

## 16) Binary search

```cpp
class Solution {
public:
    int fn(vector<int>& arr, int target) {
        int left = 0, right = arr.size() - 1;

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
};
```

## 17) Binary search: duplicate elements, left-most insertion point

```cpp
class Solution {
public:
    int fn(vector<int>& arr, int target) {
        int left = 0, right = arr.size();

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
};
```

## 18) Binary search: duplicate elements, right-most insertion point

```cpp
class Solution {
public:
    int fn(vector<int>& arr, int target) {
        int left = 0, right = arr.size();

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
};
```

## 19) Binary search: for greedy problems

```cpp
class Solution {
    // 判斷 mid 是否滿足貪心條件
    bool check(int mid, vector<int>& arr) {
        // TODO: 依題意實作
        return true;
    }

public:
    int fn(vector<int>& arr) {
        int left = 1;       // 答案下界
        int right = 1e6;    // 答案上界

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
};
```

## 20) Backtracking

```cpp
class Solution {
    vector<vector<int>> ans;

    void backtrack(vector<int>& nums, int start, vector<int>& curr) {
        // 達到終止條件時記錄答案
        ans.push_back(curr);

        for (int i = start; i < nums.size(); i++) {
            curr.push_back(nums[i]);      // 選擇
            backtrack(nums, i + 1, curr); // 遞迴
            curr.pop_back();              // 撤銷選擇（回溯）
        }
    }

public:
    vector<vector<int>> fn(vector<int>& nums) {
        vector<int> curr;
        backtrack(nums, 0, curr);
        return ans;
    }
};
```

## 21) Dynamic programming: top-down memoization

```cpp
class Solution {
    unordered_map<int, int> memo;

    int dp(vector<int>& arr, int i) {
        if (i >= arr.size()) return 0; // base case
        if (memo.count(i)) return memo[i]; // 已計算則直接返回

        int ans = max(
            dp(arr, i + 1),           // 不選 arr[i]
            arr[i] + dp(arr, i + 2)   // 選 arr[i]（依題意決定跳幾步）
        );

        return memo[i] = ans;
    }

public:
    int fn(vector<int>& arr) {
        return dp(arr, 0);
    }
};
```

> **Bottom-up 轉換步驟：**
> 1. 依狀態變數大小初始化 `dp[]` 陣列
> 2. 設定 base case（通常初始化為 0）
> 3. 從 base case 往答案方向迭代（注意方向）
> 4. 將 `dp(...)` 呼叫改寫為 `dp[...]` 存取
> 5. 回傳 `dp[目標狀態]`

```cpp
class Solution {
public:
    int fnBottomUp(vector<int>& arr) {
        int n = arr.size();
        vector<int> dp(n + 2, 0); // 多開兩格避免 index 越界

        for (int i = n - 1; i >= 0; i--) {
            dp[i] = max(dp[i + 1], arr[i] + dp[i + 2]);
        }

        return dp[0];
    }
};
```

## 22) Build a trie

```cpp
struct TrieNode {
    TrieNode* children[26] = {};
    bool isEnd = false; // 標記單詞結尾
};

class Trie {
    TrieNode* root = new TrieNode();

public:
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) {
                node->children[idx] = new TrieNode();
            }
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    bool search(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return node->isEnd;
    }

    bool startsWith(const string& prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return true;
    }
};
```

## 23) Dijkstra's algorithm

```cpp
class Solution {
public:
    vector<int> fn(vector<vector<int>>& edges, int n, int src) {
        // 建立鄰接表：graph[u] = {(v, weight), ...}
        vector<vector<pair<int,int>>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back({edge[1], edge[2]});
        }

        vector<int> dist(n, INT_MAX);
        dist[src] = 0;

        // 最小堆：{距離, 節點}
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        pq.push({0, src});

        while (!pq.empty()) {
            auto [d, node] = pq.top(); pq.pop();

            if (d > dist[node]) continue; // 已有更短路徑，跳過

            for (auto [next, weight] : graph[node]) {
                int newDist = dist[node] + weight;
                if (newDist < dist[next]) {
                    dist[next] = newDist;
                    pq.push({newDist, next});
                }
            }
        }

        return dist; // dist[i] 為 src 到節點 i 的最短距離
    }
};
```

ref:
https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/
