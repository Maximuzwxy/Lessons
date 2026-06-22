"""根据 guide_modules.json 的学习路径标签，补充 usaco_bronze_db.json 中缺失的标签。"""

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
    "sets-maps": None,           # 无对应标签
    "casework": "ad_hoc",
    "greedy": "greedy",
    "graphs": "graph",
    "rect-geo": "geometry",
    "ad-hoc": "ad_hoc",
}

# 收集每个 cpid 在学习路径中期望的标签
module_cpid_tags = {}
for mod in guide["modules"]:
    mod_id = mod["id"]
    expected_tag = MODULE_TAG_MAP.get(mod_id)
    if expected_tag is None:
        continue
    all_problems = mod.get("focus_problems", []) + mod.get("problems", [])
    for p in all_problems:
        cpid = p["cpid"]
        if cpid not in module_cpid_tags:
            module_cpid_tags[cpid] = set()
        module_cpid_tags[cpid].add(expected_tag)

# 建立 cpid -> db index
cpid_to_idx = {}
for i, p in enumerate(db["problems"]):
    if p.get("cpid"):
        cpid_to_idx[p["cpid"]] = i

# 补充缺失标签
updated = 0
for cpid, expected_tags in sorted(module_cpid_tags.items()):
    if cpid not in cpid_to_idx:
        print(f"  ✗ cpid={cpid} 不在数据库中")
        continue
    idx = cpid_to_idx[cpid]
    current = set(db["problems"][idx].get("tags", []))
    new_tags = current | expected_tags  # 合并，不删除
    if new_tags != current:
        added = new_tags - current
        db["problems"][idx]["tags"] = sorted(new_tags)
        updated += 1
        print(f"  ✓ [{cpid}] {db['problems'][idx]['name']}: +{sorted(added)}")

# 保存
with open(os.path.join(DIR, "data", "usaco_bronze_db.json"), "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"\n共更新 {updated} 道题，标签以学习路径为准已补充。")
