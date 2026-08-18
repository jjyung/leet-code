---
name: leetcode-solution-writer
description: Write or complete LeetCode solution Markdown files with Java code and Traditional Chinese explanations. Use when the user asks to add a solution, explanation, algorithm, Java implementation, complexity analysis, or documentation for a LeetCode problem in a repository.
---

# LeetCode Solution Writer

撰寫或補完 LeetCode 題解文件，預設使用 Java 程式碼與繁體中文說明。

## Workflow

1. 讀取目標檔案與最近的 repository instructions（例如 `AGENTS.md`），先保留既有題目敘述的語言與核心內容，再整理格式。
2. 從檔名、題目敘述或 LeetCode 連結確認題號、題名與難度；不要在未確認時猜測題意。
3. 選擇適合的演算法，說明核心觀察、資料結構、指標／迴圈不變量，以及為何能得到正確答案。
4. 補上可直接提交到 LeetCode 的 Java `class Solution`。除非題目要求，避免加入 `package`、`main` 或不必要的輸入輸出程式。
5. 在說明中明確標示時間複雜度與空間複雜度，並定義複雜度中的 `n`。
6. 檢查 Java 語法、邊界條件、Markdown code fence 與文件標題；必要時以最小範例驗證邏輯。

## Markdown Rules

遵循專案既有規範；若 repository instructions 有更具體要求，以其為準：

- 檔名使用三位數題號與英文題名：`<id3>. <title>.md`。
- 第一個 H1 必須與檔名（去除 `.md`）完全一致，不加 `Top Interview 150 -` 前綴。
- 中文使用繁體中文（zh-TW）。保留題目原文的英文專有名詞與程式識別字。
- `Problem` 區塊維持英文，包含題目敘述、輸入輸出、限制條件與範例；不要將題目翻譯成中文。這是為了讓讀者維持與 LeetCode 上機考試一致的英文讀題習慣，避免只習慣中文後無法理解英文題意。
- 英文題目可以整理成清楚、易讀的 Markdown，不必逐字保留原始純文字排版。可使用段落、條列、表格、`inline code`、以及 Java／text code block 呈現輸入輸出與範例，但不得改變題意、數值、變數名稱或範例結果。
- 每個範例的 `Input`、`Output`、`Explanation` 與其他範例內容，必須完整放在獨立的 `text` code block 內；`Example` 標題置於 code block 外。
- 移除無意義的換行與只含空白的行；標題、段落、列表與 code block 之間只保留 Markdown 結構所需的單一空行，不要在 code block 內任意刪除必要內容。
- 範例使用以下格式，讓輸入、輸出與解釋容易掃讀：

````md
### Example 1

```text
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with a length of 3.
```
````

- `Answer` 區塊的解題思路、程式碼說明與複雜度分析使用繁體中文；Java 程式碼、方法名稱、變數名稱與 LeetCode API 保持原樣。
- 難度使用彩色標籤：Easy `#16a34a`、Medium `#f59e0b`；若規範支援其他難度，沿用該規範。
- 建議結構：`Problem`、難度、題目敘述／連結、`Answer`、解題思路、Java 程式碼、說明與複雜度。

標籤範例：

```md
<span style="color: #16a34a;"><strong>Easy</strong></span>
```

## Java Guidance

- `String` 內容比較必須使用 `.equals()` 或安全的 `Objects.equals()`，不可用 `==`；`==` 比較的是物件參考，即使字串常值可能共用 String Pool，也不能依賴此行為。
- 正確處理空陣列、單一元素、長度不符、重複值、負數與題目允許的極端輸入。
- 依題目限制選擇 `int` 或 `long`，避免乘法或累加溢位。
- 若使用 `HashMap`、`HashSet` 等 Java 標準類別，加入必要的 `import`；保持程式碼可讀且可編譯。
- 說明程式碼中的關鍵判斷，不要只逐行翻譯程式碼。

## Scope

本技能負責建立或修改題解內容。不要自行 commit、push、修改索引或處理無關檔案，除非使用者明確要求。
