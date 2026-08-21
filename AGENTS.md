# AGENTS Guide for This Repo

本文件定義本專案中題解整理的標準流程，供後續 AI agent 或人工維護時遵循。

## Scope

- Repository: `leet-code`
- Primary content area: `top-150-interview/**`
- Current normalized folder: `top-150-interview/array-string`

## Authorization and File Scope

- 本專案以 repository 根目錄為預設工作範圍。
- 即使執行環境提供 full access，也不代表使用者已授權操作專案外的檔案。
- 在讀取、建立、修改、刪除、搬移或以其他方式操作專案外檔案前，必須先向使用者說明目標與原因，並取得明確同意。
- 若任務可在專案內完成，優先限制在專案內；不得因方便而擴大操作範圍。
- 未取得同意時，遇到需要專案外檔案的情況應先暫停並詢問，不得自行假設授權。
- 執行 `git`、測試或其他命令時，也要避免讓命令修改專案外的檔案；若無法避免，先取得使用者同意。

## Canonical File Rules

1. 檔名格式
- 使用 LeetCode 三位數題號與英文題名：`<id3>. <title>.md`
- 題號不足三位時補零（例如 `6 -> 006`、`28 -> 028`）。
- 範例：`028. Find the Index of the First Occurrence in a String.md`

2. H1 標題格式
- 第一個 H1 必須與檔名（去掉 `.md`）完全一致。
- 禁止前綴：`X. Top Interview 150 - `。
- 正確範例：`# 028. Find the Index of the First Occurrence in a String`

3. 語言規範
- 中文內容統一使用繁體中文（zh-TW）。
- 不混用簡體。

4. 難易度顯示規範
- Easy 使用綠色：
  - `<span style="color: #16a34a;"><strong>Easy</strong></span>`
- Medium 使用橘色：
  - `<span style="color: #f59e0b;"><strong>Medium</strong></span>`

## Recommended Markdown Structure

```md
# <id3>. <title>

## Problem

<span style="color: #16a34a;"><strong>Easy</strong></span>

<problem statement>

<leetcode url>

## Answer

<解題思路>

```java
<class Solution ...>
```

### 說明

1. <重點一>
2. <重點二>
```

## Quality Checklist (Per File)

- H1 與檔名一致。
- 無 `Top Interview 150 -` 前綴。
- 難易度是彩色標籤（Easy/Medium）。
- 中文為繁體。
- Java 程式碼可編譯（至少語法正確）。
- Java 程式碼必須補上繁體中文註解，說明關鍵流程；DP 題需註解狀態與轉移，Greedy 題需註解選擇策略，其他題型需註解主要資料結構或迴圈用途。
- 說明段落有時間與空間複雜度（建議補齊）。

## Category Index Rules

1. 每個題型資料夾應有 `README.md` 作為索引表。
2. 索引表至少包含三欄：`題目名稱`、`難易度`、`連結`。
3. `題目名稱` 取自各題檔案第一個 H1。
4. `難易度` 使用題內既有彩色標籤（Easy 綠、Medium 橘）。
5. `連結` 必須為相對路徑，且檔名空白需轉碼為 `%20`，避免 Markdown 連結失效。
6. 建議按題號排序，便於快速查找與複習。

### Index Table Template

```md
# <Category> Index

此索引整理 `<folder>` 的題目、難易度與連結。

| 題目名稱 | 難易度 | 連結 |
| --- | --- | --- |
| 006. Zigzag Conversion | <span style="color: #f59e0b;"><strong>Medium</strong></span> | [006. Zigzag Conversion](./006.%20Zigzag%20Conversion.md) |
```

## Batch Workflow (Agent)

1. 掃描標題是否符合檔名。
2. 批次移除多餘前綴。
3. 簡轉繁（建議使用 OpenCC，設定 `s2twp`）。
4. 套用難易度色彩標籤。
5. 進行 regex 驗證（標題、難易度、簡體殘留字）。
6. 提交前檢查 `git status`，僅提交本次目標資料夾。

## Suggested Commands

```bash
# 1) 檢查 H1
for f in top-150-interview/array-string/*.md; do
  echo "$f"; rg -n '^# ' "$f" -m1;
done

# 2) 移除標題前綴
perl -pi -e 's/^# \d+\\?\. Top Interview 150 - /# /' top-150-interview/array-string/*.md

# 3) 難易度著色
perl -0pi -e 's/^Easy$/<span style="color: #16a34a;"><strong>Easy<\/strong><\/span>/mg; s/^Medium$/<span style="color: #f59e0b;"><strong>Medium<\/strong><\/span>/mg' top-150-interview/array-string/*.md

# 4) 簡轉繁
for f in top-150-interview/array-string/*.md; do
  opencc -i "$f" -o "$f.tmp" -c s2twp.json && mv "$f.tmp" "$f"
done

# 5) 產生題型索引表（README.md）
{
  echo '# Array/String Index'
  echo ''
  echo '此索引整理 `top-150-interview/array-string` 的題目、難易度與連結。'
  echo ''
  echo '| 題目名稱 | 難易度 | 連結 |'
  echo '| --- | --- | --- |'
  find top-150-interview/array-string -maxdepth 1 -type f -name '*.md' -print0 \
    | while IFS= read -r -d '' p; do
        b=$(basename "$p")
        [ "$b" = 'README.md' ] && continue
        title=$(rg '^# ' "$p" -m1 | sed 's/^# //')
        diff=$(rg '^<span style="color: #[0-9a-f]{6};"><strong>(Easy|Medium|Hard)</strong></span>$' "$p" -m1 || true)
        [ -z "$diff" ] && diff='Unknown'
        url=${b// /%20}
        printf '| %s | %s | [%s](./%s) |\n' "$title" "$diff" "$title" "$url"
      done | sort -t '|' -k2,2V
} > top-150-interview/array-string/README.md
```

## Extension Plan

- 後續可將同一規則擴展到：
  - `top-150-interview/binary-tree`
  - `top-150-interview/graph`
  - `top-150-interview/hashmap`
  - `top-150-interview/intervals`
  - `top-150-interview/linkedlist`
  - `top-150-interview/matrix`
  - `top-150-interview/sliding-window`
  - `top-150-interview/stack`
  - `top-150-interview/trie`
  - `top-150-interview/two-pointers`
