# Binary Tree General Index

此索引整理 `top-150-interview/binary-tree-general` 的題目，並提供一般二元樹遞迴、建樹與遍歷的複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 106. Construct Binary Tree from Inorder and Postorder Traversal | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [106. Construct Binary Tree from Inorder and Postorder Traversal](./106.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal.md) |
| 226. Invert Binary Tree | <span style="color: #16a34a;"><strong>Easy</strong></span> | [226. Invert Binary Tree](./226.%20Invert%20Binary%20Tree.md) |

## 解題思路提示

先確認題目需要的是「目前節點的局部處理」還是「左右子樹回傳資訊」：

1. 定義遞迴函式輸入與回傳值，例如「處理這棵樹後回傳的新根」或「子樹的某項統計」。
2. 處理 `null` 節點這個 base case。
3. 先遞迴左右子樹，再用結果組合目前節點答案；或先處理目前節點再往下走。
4. 若題目給出遍歷序列，利用 preorder/postorder 決定根，再用 inorder 切分左右子樹。

## 必要資料結構與演算法

- **`TreeNode`**：節點通常包含 `val`、`left`、`right`。
- **DFS 遞迴**：最自然地表達子樹問題，時間通常為 $O(n)$，`n` 是節點數。
- **HashMap**：建樹時將 inorder 值映射到索引，讓每次切分可在 $O(1)$ 找到根的位置。
- **呼叫堆疊**：遞迴空間為 $O(h)$，`h` 是樹高；退化成鏈狀時為 $O(n)$，平衡時約為 $O(\log n)$。

## 複習提醒

- 空樹、單節點、只有左子樹或只有右子樹都要能正確處理。
- 建樹時不要混淆 inorder 的索引範圍與 postorder 的根索引。
- 題目若要求原地修改，確認是否真的能直接交換左右子樹。
- 先畫出一個小例子，標記每次遞迴的區間與根節點，再寫程式。
