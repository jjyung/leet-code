---
name: leetcode-solution-writer
description: Write or complete LeetCode solution Markdown files with Java code and Traditional Chinese explanations. Use when the user asks to add a solution, explanation, algorithm, Java implementation, complexity analysis, or documentation for a LeetCode problem in a repository.
---

# LeetCode Solution Writer

撰寫或補完 LeetCode 題解文件，題目章節保留英文原文，答案章節使用繁體中文說明，並預設提供 Java 程式碼。

- 題目章節保留英文原文
- 題目章節保留英文原文
- 題目章節保留英文原文

## Workflow

1. 讀取目標檔案與最近的 repository instructions（例如 `AGENTS.md`），將題目內容整理在固定的 `## Problem` 章節，並保留英文原文與核心內容。
2. 從檔名、題目敘述或 LeetCode 連結確認題號、題名與難度；不要在未確認時猜測題意。
3. 選擇適合的演算法，說明核心觀察、資料結構、指標／迴圈不變量，以及為何能得到正確答案。
4. 補上可直接提交到 LeetCode 的 Java `class Solution`。除非題目要求，避免加入 `package`、`main` 或不必要的輸入輸出程式。
5. 在說明中明確標示時間複雜度與空間複雜度，並定義複雜度中的 `n`。
6. 若使用 heap、queue 或其他候選集合，清楚說明每個元素代表什麼、初始化哪些候選、移除元素後如何產生下一個候選，以及維持的資料結構不變量。
7. 檢查 Java 語法、邊界條件、Markdown code fence 與文件標題；必要時以最小範例驗證邏輯。
8. 完成後執行 Review 階段，依照下方檢查表確認必要章節、範例格式、程式碼與內容一致性；未通過前不要交付文件。

## Review

完成題解後，必須逐項確認以下內容：

### 必要章節

- 第一個 H1 存在，且與檔名（去掉 `.md`）完全一致。
- `## Problem` 存在（固定使用此標題，不使用 `## Question`），並依序包含：難度標籤、英文原文題目敘述、限制條件、英文範例與 LeetCode 題目連結。
- `## Answer` 存在，且其解題思路、程式碼註解與複雜度說明使用繁體中文；內容包含 `### 解題思路`、Java 程式碼區塊，以及複雜度說明。
- 複雜度說明必須涵蓋關鍵判斷、邊界條件、時間複雜度與空間複雜度，並定義複雜度中的 `n`。

若原始題目沒有明確列出限制條件，先從可靠的題目來源確認；無法確認時不要自行捏造數值。

### Example 格式

每個範例都必須使用以下格式：

````md
### Example 1

```text
Input: nums = [1,3,5,6], target = 5
Output: 2
Explanation: The target 5 is found at index 2.
```
````

- `Input`、`Output` 與 `Explanation` 必須放在同一個獨立的 `text` code block 中，不使用 inline code 取代。
- `Example` 標題必須置於 code block 外。
- `Explanation` 必須與該範例的輸入和輸出一致，且範例內容維持英文。
- 不得改變題目原有的變數名稱、數值或輸出結果。

### 程式碼與內容

- Java 程式碼使用可直接提交的 `class Solution`，不包含 `package`、`main` 或除題目要求外的輸入輸出程式。
- Java code fence 已正確閉合，且關鍵流程有繁體中文註解。
- 解題思路描述的演算法、程式碼實作與複雜度分析彼此一致。
- 檢查空陣列、單一元素、邊界索引、重複值、負數與題目允許的極端輸入等適用的邊界條件。
- 若使用壓縮資料結構（例如 `int[]` 儲存多個欄位），必須在程式碼附近明確寫出欄位格式，例如 `[sum, rowIndex, columnIndex]`；並說明每個 heap 元素是一個完整物件，而不是多個分開的 heap 元素。
- 若壓縮資料結構使用數字索引，應使用具名常數（例如 `SUM_INDEX`、`ROW_INDEX`）取代難以理解的 magic number，並在建立、取出與更新候選的位置補上繁體中文註解。
- `## Problem` 區塊的題目敘述、限制條件、`Input`、`Output`、`Explanation` 與範例內容必須使用英文原文；`## Answer` 區塊的解說、程式碼註解與複雜度分析必須使用繁體中文。
- 執行 Markdown whitespace／fence 檢查，並確認只修改使用者指定的題解檔案。

## Markdown Rules

遵循專案既有規範；若 repository instructions 有更具體要求，以其為準：

- 檔名使用三位數題號與英文題名：`<id3>. <title>.md`。
- 第一個 H1 必須與檔名（去除 `.md`）完全一致，不加 `Top Interview 150 -` 前綴。
- 中文使用繁體中文（zh-TW）。保留題目原文的英文專有名詞與程式識別字。
- `## Problem` 區塊維持英文原文，包含題目敘述、輸入輸出、限制條件與範例；不要將題目翻譯成中文。這是為了讓讀者維持與 LeetCode 上機考試一致的英文讀題習慣，避免只習慣中文後無法理解英文題意。
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

- `## Answer` 區塊的解題思路、程式碼註解、邊界條件與複雜度分析使用繁體中文；Java 程式碼、方法名稱、變數名稱與 LeetCode API 保持原樣。
- 難度使用彩色標籤：Easy `#16a34a`、Medium `#f59e0b`；若規範支援其他難度，沿用該規範。
- 建議結構：`Problem`、難度、英文原文題目敘述／連結、`Answer`、繁體中文解題思路、Java 程式碼、說明與複雜度。

標籤範例：

```md
<span style="color: #16a34a;"><strong>Easy</strong></span>
```

## Java Guidance

- `String` 內容比較必須使用 `.equals()` 或安全的 `Objects.equals()`，不可用 `==`；`==` 比較的是物件參考，即使字串常值可能共用 String Pool，也不能依賴此行為。
- 正確處理空陣列、單一元素、長度不符、重複值、負數與題目允許的極端輸入。
- 依題目限制選擇 `int` 或 `long`，避免乘法或累加溢位。
- 若使用 `HashMap`、`HashSet` 等 Java 標準類別，加入必要的 `import`；保持程式碼可讀且可編譯。
- 說明程式碼中的關鍵判斷，不要只逐行翻譯程式碼；註解應回答「這個資料代表什麼」、「為什麼可以這樣初始化」以及「下一步為什麼這樣產生」。
- 優先使用具名欄位或小型類別表達複合狀態。若為符合 LeetCode 寫法或題解教學目的而使用 `int[]` tuple，必須同步提供欄位索引常數與欄位格式註解，不得留下需要讀者自行猜測的 `candidate[0]`、`candidate[1]`、`candidate[2]`。
- 對 heap 題，至少在程式碼中註解：heap 儲存的單位、比較依據、初始候選的來源、`poll` 後新增候選的規則，以及為何這些候選足以涵蓋下一個答案。
- 避免為了縮短程式碼而犧牲可讀性；變數名稱應表達角色，例如 `currentCandidate`、`nextCandidate`、`rowIndex`、`columnIndex`，而不是只使用難以追蹤的縮寫。

## Scope

本技能負責建立或修改題解內容。不要自行 commit、push、修改索引或處理無關檔案，除非使用者明確要求。
