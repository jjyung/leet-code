# Binary Search Tree Index

此索引整理 `top-150-interview/binary-search-tree` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 230. Kth Smallest Element in a BST | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [230. Kth Smallest Element in a BST](./230.%20Kth%20Smallest%20Element%20in%20a%20BST.md) |
| 530. Minimum Absolute Difference in BST | <span style="color: #16a34a;"><strong>Easy</strong></span> | [530. Minimum Absolute Difference in BST](./530.%20Minimum%20Absolute%20Difference%20in%20BST.md) |

## 解題思路提示

BST 題最重要的性質是：**inorder traversal 會按照遞增順序走訪節點**。

1. 先確認題目是否能直接轉成「排序序列上的問題」。
2. Kth smallest 類題用 inorder 計數，走到第 `k` 個節點即可停止。
3. 最小差值類題只需記住上一個 inorder 節點，計算相鄰值差。
4. 若要搜尋特定值，利用目前節點與目標的大小關係往左或右走。

## 必要資料結構與演算法

- **BST**：左子樹值小於根、右子樹值大於根；實際重複值規則要依題目確認。
- **Inorder DFS**：遞迴或 `Deque<TreeNode>` 迭代實作，依序產生排序值。
- **前驅狀態**：保存上一個走訪節點或值，就能在線性時間完成相鄰差值比較。
- **複雜度**：完整走訪為 $O(n)$ 時間；額外空間為 $O(h)$，`h` 是樹高，迭代 stack 可提早停止。

## 複習提醒

- 不要把一般二元樹的 preorder 當成排序順序；只有 BST 的 inorder 才有此性質。
- 只有一個節點時沒有相鄰差值，初始化前一個值要避免誤算。
- 退化樹可能讓遞迴深度達到 $O(n)$，極端限制下考慮迭代寫法。
- 測試空樹、最小/最大值、重複值規則與 `k = 1`、`k = n`。
