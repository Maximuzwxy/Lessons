"""
扫描 Bronze 目录下所有 .py 文件，将 local_file 字段同步到数据库中。
"""

import json
import os

BRONZE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "usaco_bronze_db.json")

def find_py_files():
    """扫描 Bronze 目录下所有 .py 文件（排除 dashboard, ppt, __pycache__ 等）"""
    py_files = []
    for root, dirs, files in os.walk(BRONZE_DIR):
        dirs[:] = [d for d in dirs if d not in ("dashboard", "ppt", "__pycache__", "my_package")]
        for f in files:
            if f.endswith(".py") and not f.startswith("lesson") and f not in ("my_tools.py", "test.py", "classic_problems.py", "__init__.py"):
                rel_path = os.path.relpath(os.path.join(root, f), BRONZE_DIR).replace("\\", "/")
                slug = os.path.splitext(f)[0]
                py_files.append((rel_path, slug))
    return py_files

# 文件名 -> DB slug 的手动映射（处理缩写/拼写差异）
SLUG_OVERRIDES = {
    "cow_signal": "the_cow-signal",
    "mowing_the_filed": "mowing_the_field",
    "cross_the_road": "why_did_the_cow_cross_the_road",
    "cross_the_road2": "why_did_the_cow_cross_the_road_ii",
    "cross_the_road3": "why_did_the_cow_cross_the_road_iii",
    "tic_tac_toe": "team_tic_tac_toe",
    "bucket_bridge": "bucket_brigade",
}

def main():
    py_files = find_py_files()

    with open(DB_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    # 建立 slug -> problem 索引
    slug_map = {}
    for i, p in enumerate(db["problems"]):
        slug = p.get("slug", "")
        slug_map[slug] = i

    # 先 clear 所有 local_file（防止旧文件被删后还残留）
    for p in db["problems"]:
        p["local_file"] = None

    updated = 0
    for rel_path, slug in py_files:
        # 先检查是否需要 override
        target_slug = SLUG_OVERRIDES.get(slug, slug)

        if target_slug in slug_map:
            idx = slug_map[target_slug]
            db["problems"][idx]["local_file"] = rel_path
            updated += 1
            print(f"  ✓ {slug} -> {rel_path}" + (f"  (mapped to {target_slug})" if target_slug != slug else ""))
        else:
            print(f"  ✗ {slug} ({rel_path}) — 未在数据库中找到匹配")

    # 保存
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    solved = sum(1 for p in db["problems"] if p.get("local_file"))
    total = len(db["problems"])
    print(f"\n同步完成: {updated} 条更新, 已解决 {solved}/{total} 道题")

if __name__ == "__main__":
    main()
