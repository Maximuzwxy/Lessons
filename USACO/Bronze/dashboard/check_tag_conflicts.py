"""检查 usaco_bronze_db.json 的标签是否与 guide_modules.json 冲突。"""

import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR, "data", "guide_modules.json"), "r", encoding="utf-8") as f:
    guide = json.load(f)

with open(os.path.join(DIR, "data", "usaco_bronze_db.json"), "r", encoding="utf-8") as f:
    db = json.load(f)

# 学习路径模块 -> 数据库标签 的映射
MODULE_TAG_MAP = {
    "simulation": "simulation",
    "complete-search": "brute_force",
    "complete-rec": "recursion",
    "sorting": "sorting",
    "sets-maps": None,           # 无对应标签，暂不处理
    "casework": "ad_hoc",
    "greedy": "greedy",
    "graphs": "graph",
    "rect-geo": "geometry",
    "ad-hoc": "ad_hoc",
}

# 建立 cpid -> 期望标签列表（来自学习路径）
module_cpid_tags = {}  # cpid -> [expected tags from all relevant modules]
for mod in guide["modules"]:
    mod_id = mod["id"]
    expected_tag = MODULE_TAG_MAP.get(mod_id)
    if expected_tag is None:
        continue
    all_problems = mod.get("focus_problems", []) + mod.get("problems", [])
    for p in all_problems:
        cpid = p["cpid"]
        if cpid not in module_cpid_tags:
            module_cpid_tags[cpid] = []
        if expected_tag not in module_cpid_tags[cpid]:
            module_cpid_tags[cpid].append(expected_tag)

# 建立数据库 cpid -> 当前标签
db_cpid_tags = {}
for p in db["problems"]:
    if p.get("cpid"):
        db_cpid_tags[p["cpid"]] = {
            "tags": p.get("tags", []),
            "name": p["name"],
        }

# 检查冲突：数据库中缺少学习路径期望的标签
conflicts = []
for cpid, expected_tags in module_cpid_tags.items():
    if cpid in db_cpid_tags:
        current_tags = db_cpid_tags[cpid]["tags"]
        name = db_cpid_tags[cpid]["name"]
        missing = [t for t in expected_tags if t not in current_tags]
        if missing:
            conflicts.append((cpid, name, current_tags, missing, expected_tags))

print("=" * 70)
print("标签冲突检查：数据库缺少学习路径期望的标签")
print("=" * 70)

if not conflicts:
    print("(无冲突)")

for cpid, name, current, missing, expected in sorted(conflicts):
    print(f"\n  cpid={cpid}  {name}")
    print(f"    当前标签: {current}")
    print(f"    学习路径期望: {expected}")
    print(f"    缺失标签:   {missing}")

print("\n" + "=" * 70)
print(f"共 {len(conflicts)} 道题需要补充标签")
