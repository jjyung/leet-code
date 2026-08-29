# Math Index

此索引整理 `top-150-interview/math` 的題目，並提供數學觀察、數字表示與溢位處理的複習重點。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 009. Palindrome Number | <span style="color: #16a34a;"><strong>Easy</strong></span> | [009. Palindrome Number](./009.%20Palindrome%20Number.md) |
| 066. Plus One | <span style="color: #16a34a;"><strong>Easy</strong></span> | [066. Plus One](./066.%20Plus%20One.md) |
| 172. Factorial Trailing Zeroes | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [172. Factorial Trailing Zeroes](./172.%20Factorial%20Trailing%20Zeroes.md) |

## 解題思路提示

數學題先尋找「答案由哪些因子或位數決定」，再決定是否需要真的建立完整數值：

1. 把十進位數字拆成個位數，或用除法與取餘數逐位處理。
2. 找出不變量，例如反轉一半數字、因數配對或尾端零的來源。
3. 用題目限制判斷 `int`、`long` 或字串運算是否必要。
4. 用小數字手算驗證公式，再處理負數、前導零與邊界值。

## 必要資料結構與演算法

- **取餘數與整除**：`number % 10` 取得末位，`number / 10` 移除末位。
- **因數分解觀察**：階乘尾端零來自 `10 = 2 * 5`，通常只需計算 5 的冪次數。
- **字串/陣列進位**：從最低位開始處理 carry，避免把大數轉成原生數值。
- **複雜度**：逐位或逐個 5 的冪次處理通常為 $O(\log n)$ 時間、$O(1)$ 額外空間。

## 複習提醒

- 負數是否算回文、末尾零是否改變數字意義，都要依題目定義處理。
- `Integer.MIN_VALUE` 取負可能溢位，反轉數字前先檢查型別範圍。
- Plus One 的進位可能一路傳到最前面，別忘記陣列長度增加的情況。
- 公式題不要只背結論，要能說明為什麼只數某一類因子就足夠。
