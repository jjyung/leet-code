# HashMap Index

此索引整理 `top-150-interview/hashmap` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 001. Two Sum | <span style="color: #16a34a;"><strong>Easy</strong></span> | [001. Two Sum](./1.%20Two%20Sum.md) |
| 049. Group Anagrams | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [049. Group Anagrams](./049.%20Group%20Anagrams.md) |
| 205. Isomorphic Strings | <span style="color: #16a34a;"><strong>Easy</strong></span> | [205. Isomorphic Strings](./205.%20Isomorphic%20Strings.md) |
| 242. Valid Anagram | <span style="color: #16a34a;"><strong>Easy</strong></span> | [242. Valid Anagram](./242.%20Valid%20Anagram.md) |
| 290. Word Pattern | <span style="color: #16a34a;"><strong>Easy</strong></span> | [290. Word Pattern](./290.%20Word%20Pattern.md) |
| 383. Ransom Note | <span style="color: #16a34a;"><strong>Easy</strong></span> | [383. Ransom Note](./383.%20Ransom%20Note.md) |

## 解題思路提示

HashMap/HashSet 題通常是在把「重複搜尋」改成「一次建立索引」：

1. 先決定 key 是數值、字元、字串，還是某個標準化後的簽名。
2. 掃描元素時查詢既有資訊，再依題意更新 map；注意查詢與更新的先後順序。
3. 需要雙向對應時使用兩張 map，例如字元到字元與字元到字元的反向映射。
4. 需要分組時，為每個元素建立相同問題會得到相同結果的 canonical key。

## 必要資料結構與演算法

- **HashMap**：平均 $O(1)$ 查詢與更新，適合 value-to-index、頻率與雙向映射。
- **HashSet**：平均 $O(1)$ 判斷是否出現過，適合去重與存在性檢查。
- **頻率陣列**：字元範圍固定時比 HashMap 更簡單且常數較小，空間為 $O(\Sigma)$。
- **複雜度**：一次掃描通常為 $O(n)$ 時間、$O(n)$ 空間；`n` 是元素或字元數量，`\Sigma` 是字元集合大小。

## 複習提醒

- Java 的 `HashMap` 平均是 $O(1)$，但要正確處理不存在的 key 與頻率歸零。
- Group Anagrams 的 key 必須讓同組字串產生相同結果，可用排序字串或字母計數簽名。
- 同構字串與 Word Pattern 不只要求單向映射，還要避免兩個來源映射到同一個目標。
- 檢查重複值、空字串、長度不一致與答案不存在的情況。
