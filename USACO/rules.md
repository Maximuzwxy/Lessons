# USACO 代码注释规范

## 工作流程

### 1. 获取题目信息
- **必须**从 USACO 官网获取题目原文描述、输入输出格式、数据范围、示例
- **必须**在文件顶部 docstring 中包含题目链接（如 `http://www.usaco.org/index.php?page=viewproblem2&cpid=XXX`）
- **必须**在 docstring 中标注 Tags 标签（如 Ad Hoc, Geometry, 2D Grid 等）
- **必须**在 docstring 中标注 Difficulty（取值 very_easy / easy / normal / hard / very_hard，与数据库中一致）

### USACO 资源链接速查

题目、题解、测试数据均可通过 cpid 和题目简称定位：

| 资源 | URL 格式 |
|---|---|
| 题目页面 | `https://www.usaco.org/index.php?page=viewproblem2&cpid={cpid}` |
| 官方题解 | `https://www.usaco.org/current/data/sol_{shortname}_bronze_{contest}18.html` |
| 测试数据 (zip) | `https://www.usaco.org/current/data/{shortname}_bronze_{contest}18.zip` |
| 比赛结果页（含所有题目链接） | `https://www.usaco.org/current/index.php?page={contest}18results` |

其中 `{contest}` 为 `open`（US Open）、`dec`（December）、`jan`（January）、`feb`（February）之一；`{shortname}` 为题目英文名的简短形式（如 milking order → `milkorder`，family tree → `family`）。具体名称可从比赛结果页的链接中确认。

测试数据 zip 解压后为若干 `.in` / `.out` 文件对（如 `1.in`、`1.out`、...），可用 `cp` 将单个 case 复制为 `family.in` 后运行程序调试。

### 2. 理解题目和算法
- 仔细阅读官网的题目描述
- 结合用户提供的代码，理解算法思路
- 不要臆测或编造任何信息

### 3. 编写注释和解析
- **必须使用英文**编写所有注释、docstring 和题目解析（包括 Solution 标题、思路描述、代码注释等）
- 只写从官网获取的正确信息
- Example 必须与官网完全一致
- 数据范围必须与官网完全一致

### 4. 同步 Dashboard 数据库
完成代码注释后，**必须**检查并更新同路径下的 `dashboard/data/usaco_bronze_db.json`：
- 检查该题目的 `tags` 标签是否需要**新增**或**修改**（例如：根据算法特点补充 `geometry`、`ad_hoc`、`2d_grid` 等标签）
- 检查 `local_file` 字段是否需要更新为实际的 `.py` 文件路径
- 如有其他元数据需要同步（如 `difficulty`、`notes`），也应一并处理
- 确保 `.py` 文件头部的 Tags 与数据库中的 tags 保持一致

**重要：编辑 JSON 数据库时的注意事项**

由于 JSON 文件中有多个题目，同一年份、同一月份的不同题目往往有相同的 `year`、`contest`、`difficulty` 等字段，`SearchReplace` 只会替换**第一个**匹配的片段。为避免编辑到错误的题目：

- `old_str` **必须包含 `"name"` 或 `"slug"` 字段**，这是唯一能区分同一月份不同题目的标识
- `old_str` 应至少覆盖从 `"name"` 到目标修改字段（如 `notes`）的范围，确保匹配到正确的题目
- 编辑前先用 `Grep` 带 `-C` 上下文查看目标题目在 JSON 中的确切位置

反例（可能匹配到其他题目）：
```json
      "difficulty": "easy",
      "notes": null
```
正例（带 `"name"` 唯一标识）：
```json
      "name": "Circular Barn",
      "slug": "circular_barn",
      ...
      "difficulty": "easy",
      "notes": null
```

### 5. Notes 字段处理
- **仅在用户明确提供 notes 内容时才填写**，不得自动生成或自行添加 notes
- 用户提供的 notes 可能比较口语化，**可以**在不改变原意的前提下进行润色和修饰
- 润色原则：
  - 去掉口语化的冗余表达（如"做起来非常的，用起来非常的" → "简洁直观"）
  - 保留用户想要传达的核心信息（如用到了什么数据结构、算法的特点等）
  - 保持简洁，通常 1-2 句话即可
  - 使用中文撰写
- **必须**保留用户的核心观点和评价，不得自行添加用户未提及的内容

### 6. 用户解法代码的保护原则
- **严禁直接修改**用户的 Solution 代码（包括算法逻辑、变量命名、代码结构等）
- 如果发现用户代码中存在 bug、可优化的地方或值得改进的写法：
  - **不要直接改动用户的代码**
  - 在对比分析中以文字形式指出问题和优化建议
  - 可以**建议**用户如何修改，但不替用户做修改
- 此原则**仅适用于用户解法代码**；官方解法（Solution 2）可以自由翻译和生成

## 文件结构模板

每个题目的 `.py` 文件应包含以下三个部分：

```python
"""
USACO [年份] [比赛] Contest, Bronze - Problem [编号]. [题目名称]
===================================================================
Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=XXX

Tags: [标签1], [标签2], ...

Difficulty: easy

Problem Description:
-------------------
[题目核心描述，包括输入输出格式、数据范围]

Sample Input:              Sample Output:
[官网示例输入]              [官网示例输出]

Explanation:
[样例解释，如有必要]

====================================================================
Solution 1: [用户解法的简要标题]
====================================================================
[描述用户解法的核心思路和步骤]

Time Complexity: O(...)
"""

import sys
sys.stdin = open('xxx.in', 'r')
sys.stdout = open('xxx.out', 'w')

# [用户代码，每段加上中文/英文注释]

# =====================================================================
# Solution 2: Official USACO Solution (by [作者]) — Python Translation
# =====================================================================
# [官方解法的思路描述]
#
# Time Complexity: O(...)

# [官方代码的 Python 翻译版本，整体注释掉]
# import sys
# sys.stdin = open('xxx.in', 'r')
# sys.stdout = open('xxx.out', 'w')
# ...
```

## 各部分详细要求

### Part 1: 题目解析（文件顶部 docstring）
- 题目名称、编号、比赛信息
- **题目链接**（USACO 官网 cpid）
- **Tags 标签**（英文，如 Ad Hoc, Geometry, Simulation, Brute Force, 2D Grid 等）
- **Difficulty**（取值 very_easy / easy / normal / hard / very_hard，从数据库中同步）
- 题目描述、输入输出格式、数据范围
- 官网 Sample Input/Output（必须与官网完全一致）
- 如有必要，附带样例解释

### Part 2: 用户解法（Solution 1）
- **必须**给出算法名称或简短标题
- **必须**描述核心思路和关键步骤
- **必须**标注时间复杂度
- **必须**给代码中的关键部分加上注释
- 这是**激活状态**的代码（非注释），可直接运行

### Part 3: 官方解法（Solution 2）
- 从 USACO 官网获取官方题解
- **如果官方已有 Python 代码**：直接复制，加上注释
- **如果官方是 C++/Java**：翻译成等价的 Python 代码，加上注释
- 官方解法的代码整体**注释掉**（每行前加 `#`），只作为参考
- **必须**描述官方解法的思路和与用户解法的差异

## 禁止事项

- ❌ 不得自行编造数据范围
- ❌ 不得自行编造示例输入输出
- ❌ 不得在示例中出现中文（除非题目本身是中文）
- ❌ 不得在未访问官网的情况下写解析
- ❌ 不得遗漏题目链接

## 参考示例

参见以下已完成的文件：
- `2017/December/blocked_billboard.py` — 包含用户像素标记法 + 官方矩形求交法
- `2017/us_open/modern_art.py` — 包含依赖图计数法 + 排列暴力法 + 官方解法
- `2016/us_open/bull_in_a_china_shop.py` — 包含 DFS 位移法 + 官方暴力枚举法
