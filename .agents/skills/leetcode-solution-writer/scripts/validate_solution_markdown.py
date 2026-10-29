#!/usr/bin/env python3
"""Check the required Markdown structure of one LeetCode solution file."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_solution_markdown.py <solution.md>")

    path = Path(sys.argv[1])
    if not path.is_file():
        fail(f"file not found: {path}")

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    first_heading = next((line[2:].strip() for line in lines if line.startswith("# ")), None)
    if first_heading != path.stem:
        fail(f"first H1 must exactly match filename stem ({path.stem!r})")

    if "## Problem" not in text or "## Answer" not in text:
        fail("required headings ## Problem and ## Answer must both exist")
    problem_start = text.index("## Problem")
    answer_start = text.index("## Answer")
    if answer_start <= problem_start:
        fail("## Problem must appear before ## Answer")

    problem = text[problem_start:answer_start]
    answer = text[answer_start:]

    if not re.search(r"(?m)^<span style=\"color: #[0-9a-fA-F]{6};\"><strong>(Easy|Medium|Hard)</strong></span>$", text):
        fail("a supported colored difficulty label must appear before ## Problem")
    if not re.search(r"(?im)^\s*Constraints\s*:", problem):
        fail("## Problem must include the original Constraints section")
    if not re.search(r"https?://leetcode\.com/problems/[^\s)>]+", problem):
        fail("## Problem must include a LeetCode problem URL")

    examples = list(re.finditer(r"(?m)^### Example\s+\d+\s*$", problem))
    if not examples:
        fail("## Problem must contain at least one ### Example heading")
    for index, match in enumerate(examples):
        end = examples[index + 1].start() if index + 1 < len(examples) else len(problem)
        section = problem[match.end():end]
        blocks = re.findall(r"```text\s*\n(.*?)\n```", section, flags=re.DOTALL)
        if len(blocks) != 1:
            fail(f"{match.group().strip()} must have exactly one text code block")
        block = blocks[0]
        for field in ("Input:", "Output:", "Explanation:"):
            if not re.search(rf"(?m)^{re.escape(field)}\s*\S", block):
                fail(f"{match.group().strip()} text block must contain {field}")

    if "### 解題思路" not in answer:
        fail("## Answer must include ### 解題思路")
    if "時間複雜度" not in answer or "空間複雜度" not in answer:
        fail("## Answer must explain time and space complexity")
    java_blocks = re.findall(r"```java\s*\n(.*?)\n```", answer, flags=re.DOTALL)
    if len(java_blocks) != 1 or "class Solution" not in java_blocks[0]:
        fail("## Answer must contain exactly one fenced Java class Solution")
    if len(re.findall(r"(?m)^```", text)) % 2:
        fail("Markdown code fences are not balanced")
    if any(line.rstrip(" \t") != line for line in lines):
        fail("trailing whitespace found")
    if any(line.strip() == "" and line != "" for line in lines):
        fail("whitespace-only line found")

    print(f"PASS: required Markdown structure checked in {path}")
    print("Manual review still required for source fidelity, Traditional Chinese, Java logic, and image preservation.")


if __name__ == "__main__":
    main()
