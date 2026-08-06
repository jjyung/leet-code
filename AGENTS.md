# AGENTS Guide for This Repo

本文件定義本專案中題解整理的標準流程，供後續 AI agent 或人工維護時遵循。

## Scope

- Repository: `leet-code`
- Primary content area: `top-150-interview/**`
- Current normalized folder: `top-150-interview/array-string`

## Canonical File Rules

1. 檔名格式
- 使用 LeetCode 題號與英文題名：`<id>. <title>.md`
- 範例：`28. Find the Index of the First Occurrence in a String.md`

2. H1 標題格式
- 第一個 H1 必須與檔名（去掉 `.md`）完全一致。
- 禁止前綴：`X. Top Interview 150 - `。
- 正確範例：`# 28. Find the Index of the First Occurrence in a String`

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
# <id>. <title>

## Question

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
- 說明段落有時間與空間複雜度（建議補齊）。

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
