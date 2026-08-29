# Bit Manipulation Index

此索引整理 `top-150-interview/bit-manipulation` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 067. Add Binary | <span style="color: #16a34a;"><strong>Easy</strong></span> | [067. Add Binary](./067.%20Add%20Binary.md) |
| 137. Single Number II | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [137. Single Number II](./137.%20Single%20Number%20II.md) |

## 解題思路提示

位元題先把數字視為固定寬度的 bit pattern，逐位思考，而不是只用十進位直覺：

1. 判斷題目是否可用 XOR 的交換律、結合律與 `x ^ x = 0` 消除成對元素。
2. 加法題逐位維護 carry；若是字串輸入，從最低位往最高位處理。
3. 出現次數不是 2 的倍數時，可對每個 bit 計數後取模，重建唯一數字。
4. 先釐清 Java 的 signed integer、負數補數表示與 `>>>`/`>>` 的差異。

## 必要資料結構與演算法

- **XOR**：相同 bit 得 0、不同 bit 得 1，適合找只出現一次的元素。
- **AND/OR/NOT/shift**：用於取出、設定、清除或移動 bit。
- **Bit count**：對每一個 bit 累加出現次數，再依重複次數取模。
- **複雜度**：固定 32 位整數的逐位處理可視為 $O(n)$ 時間、$O(1)$ 空間；`n` 是元素數量。

## 複習提醒

- XOR 題要確認重複次數與整數範圍；出現三次的題目不能直接套用 XOR。
- `1 << bit` 在最高位附近可能涉及 signed int，必要時使用 `long`。
- 二進位字串加法要保留 carry，迴圈結束後仍可能需要補上 `1`。
- 用 `0`、全 1、最高位、負數與重複模式手算，驗證 shift 方向。
