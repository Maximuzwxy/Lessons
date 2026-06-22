"""
USACO Bronze 题目标签自动生成脚本
根据题目名称模式自动添加标签
"""

import json
import re

# 预定义的标签映射 (基于题目名称模式)
TAG_PATTERNS = {
    # 模拟法 - 很多 Bronze 题都是模拟
    "simulation": [
        r"signal", r"paint", r"shuffle", r"tipping", r"taming",
        r"teleportation", r"hoofball", r"swap", r"photoshoot",
        r"herdle", r"sleep", r"walk", r"rut", r"stalling",
        r"comfortable", r"clock", r"tame", r"balancing", r"cannon",
        r"candy", r"cowntact", r"logic", r"walking", r"mooin",
        r"moos", r"photos", r"cow photos", r"split", r"exchange"
    ],
    # 暴力枚举
    "brute_force": [
        r"taming", r"guess", r"tame", r"angry", r"taming",
        r"reverse", r"engineering", r"alchemy", r"leaders",
        r"balancing", r"bacteria", r"productivity", r"permutation",
        r"favorite", r"cheese", r"roundabout"
    ],
    # 二维网格/图像处理
    "2d_grid": [
        r"signal", r"paint", r"grid", r"block", r"square",
        r"rectangle", r"barn", r"diamond", r"field", r"pasture",
        r"farm", r"grid", r"stamp", r"rotate", r"shift",
        r"reflection", r"mexes"
    ],
    # 排序
    "sorting": [
        r"sort", r"order", r"lineup", r"sequence", r"permutation"
    ],
    # 双指针/滑动窗口
    "two_pointers": [
        r"window", r"subarray", r"range", r"pair", r"diamond",
        r"daisy", r"chain", r"gymnastics", r"traffic"
    ],
    # 前缀和
    "prefix_sum": [
        r"prefix", r"sum", r"range", r"segment", r"cumulative"
    ],
    # BFS
    "bfs": [
        r"maze", r"grid", r"shortest", r"path", r"cowntact",
        r"tracing", r"spread", r"contagion", r"infection"
    ],
    # DFS
    "dfs": [
        r"tree", r"graph", r"connected", r"component", r"revegetation"
    ],
    # 贪心
    "greedy": [
        r"greedy", r"optimal", r"best", r"maximize", r"minimize",
        r"ranking", r"leader", r"priority"
    ],
    # 动态规划
    "dp": [
        r"dp", r"dynamic", r"partition", r"knapsack", r"coin",
        r"pails", r"operations", r"drought", r"modern art"
    ],
    # 字符串处理
    "string": [
        r"word", r"string", r"text", r"processor", r"language",
        r"evolution", r"spell", r"edit", r"acowdemia", r"uddered"
    ],
    # 数学/数论
    "math": [
        r"math", r"equation", r"formula", r"prime", r"factor",
        r"mod", r"modulo", r"remainder", r"divisible", r"count",
        r"abc", r"promotion", r"operations", r"moo operations"
    ],
    # 图论
    "graph": [
        r"graph", r"edge", r"node", r"connection", r"network",
        r"milking order", r"family tree", r"evolution", r"connected"
    ],
    # 递归
    "recursion": [
        r"recursive", r"recursion", r"fractal", r"fence"
    ],
    # 几何
    "geometry": [
        r"triangle", r"area", r"angle", r"polygon", r"circle",
        r"fence", r"pasture", r"field", r"circular", r"clockwise"
    ],
    # 位运算
    "bitwise": [
        r"bit", r"xor", r"and", r"or", r"shift", r"mask"
    ]
}

# 精确匹配的标签 (题目名称 -> 标签)
EXACT_TAG_MAP = {
    # 2015-16
    "Speeding Ticket": ["simulation", "prefix_sum"],
    "Milk Pails": ["brute_force", "dp"],
    "Diamond Collector": ["two_pointers", "sorting"],
    "Contaminated Milk": ["brute_force", "simulation"],
    "Angry Cows": ["brute_force", "simulation"],
    "Mowing the Field": ["brute_force", "simulation"],
    "Circular Barn": ["brute_force", "geometry"],
    "Load Balancing": ["brute_force"],
    "Bull in a China Shop": ["brute_force", "2d_grid"],
    "Field Reduction": ["brute_force", "geometry"],

    # 2016-17
    "Square Pasture": ["geometry", "brute_force"],
    "Block Game": ["brute_force", "simulation"],
    "The Cow-Signal": ["simulation", "2d_grid"],
    "Don't Be Last!": ["sorting", "brute_force"],
    "Hoof Paper Scissors": ["brute_force", "simulation"],
    "Cow Tipping": ["brute_force", "simulation"],
    "Why Did the Cow Cross the Road": ["simulation", "brute_force"],
    "Why Did the Cow Cross the Road II": ["simulation", "brute_force"],
    "Why Did the Cow Cross the Road III": ["simulation", "brute_force"],
    "The Lost Cow": ["brute_force", "simulation"],
    "Bovine Genomics": ["brute_force", "string"],
    "Modern Art": ["brute_force", "dp"],

    # 2017-18
    "Blocked Billboard": ["2d_grid", "brute_force"],
    "The Bovine Shuffle": ["simulation", "array"],
    "Milk Measurement": ["brute_force", "simulation"],
    "Blocked Billboard II": ["2d_grid", "brute_force"],
    "Lifeguards": ["brute_force", "interval"],
    "Out of Place": ["sorting", "brute_force"],
    "Teleportation": ["brute_force", "simulation"],
    "Hoofball": ["brute_force", "simulation"],
    "Taming the Herd": ["brute_force", "dp"],
    "Team Tic Tac Toe": ["brute_force", "simulation", "game"],
    "Milking Order": ["graph", "sorting"],
    "Family Tree": ["graph", "dfs"],

    # 2018-19
    "Mixing Milk": ["greedy", "simulation"],
    "The Bucket List": ["brute_force", "simulation"],
    "Back and Forth": ["brute_force", "simulation"],
    "Shell Game": ["brute_force", "simulation"],
    "Sleepy Cow Sorting": ["sorting", "simulation"],
    "Guess the Animal": ["string", "brute_force"],
    "Sleepy Cow Herding": ["greedy", "two_pointers"],
    "The Great Revegetation": ["graph", "dfs", "greedy"],
    "Measuring Traffic": ["simulation", "prefix_sum"],
    "Bucket Brigade": ["simulation", "string"],
    "Milk Factory": ["graph", "tree"],
    "Cow Evolution": ["graph", "tree", "string"],

    # 2019-20
    "Cow Gymnastics": ["two_pointers", "brute_force"],
    "Where Am I?": ["string", "brute_force"],
    "Livestock Lineup": ["brute_force", "sorting"],
    "Word Processor": ["string", "simulation"],
    "Photoshoot": ["math", "combinatorics"],
    "Race": ["two_pointers", "math"],
    "Triangles": ["geometry", "math"],
    "Mad Scientist": ["string", "brute_force"],
    "Swapity Swap": ["simulation", "sorting"],
    "Social Distancing I": ["greedy", "sorting"],
    "Social Distancing II": ["greedy", "interval"],
    "Cowntact Tracing": ["bfs", "graph"],

    # 2020-21
    "Do you know your ABCs?": ["math", "brute_force"],
    "Daisy Chains": ["brute_force", "two_pointers"],
    "Stuck in a Rut": ["geometry", "simulation"],
    "Uddered but not Herd": ["string", "greedy"],
    "Even More Odd Photos": ["math", "combinatorics"],
    "Just Stalling": ["brute_force", "sorting"],
    "Year of the Cow": ["string", "math"],
    "Comfortable Cows": ["simulation", "math"],
    "Clockwise Fence": ["geometry", "math"],
    "Acowdemia I": ["sorting", "math"],
    "Acowdemia II": ["sorting", "math"],
    "Acowdemia III": ["sorting", "math"],

    # 2021-22
    "Lonely Photo": ["brute_force", "simulation"],
    "Air Cowditioning": ["sorting", "greedy"],
    "Walking Home": ["bfs", "graph"],
    "Herdle": ["string", "brute_force"],
    "Non-Transitive Dice": ["brute_force", "game"],
    "Drought": ["brute_force", "dp"],
    "Sleeping in Class": ["simulation", "math"],
    "Photoshoot 2": ["math", "sorting"],
    "Blocks": ["2d_grid", "brute_force"],
    "Counting Liars": ["sorting", "brute_force"],
    "Alchemy": ["brute_force", "simulation"],

    # 2022-23
    "Cow College": ["math", "sorting"],
    "Feeding the Cows": ["brute_force", "string"],
    "Reverse Engineering": ["brute_force", "dp"],
    "Leaders": ["brute_force", "sorting"],
    "Air Cowditioning II": ["sorting", "greedy"],
    "Moo Operations": ["math", "string"],
    "Hungry Cow": ["simulation", "prefix_sum"],
    "Stamp Grid": ["2d_grid", "brute_force"],
    "Watching Mooloo": ["math", "two_pointers"],
    "FEB": ["brute_force", "simulation"],
    "Moo Language": ["string", "brute_force"],
    "Rotate and Shift": ["2d_grid", "simulation"],

    # 2023-24
    "Candy Cane Feast": ["brute_force", "simulation"],
    "Cowntact Tracing 2": ["bfs", "graph"],
    "Farmer John Actually Farms": ["brute_force", "2d_grid"],
    "Majority Opinion": ["brute_force", "sorting"],
    "Cannon Ball": ["math", "geometry"],
    "Balancing Bacteria": ["brute_force", "string"],
    "Palindrome Game": ["string", "brute_force"],
    "Milk Exchange": ["simulation", "brute_force"],
    "Maximizing Productivity": ["sorting", "greedy"],
    "Logical Moos": ["string", "brute_force"],
    "Walking Along a Fence": ["math", "geometry"],
    "Farmer John's Favorite Permutation": ["brute_force", "dp"],

    # 2024-25
    "Roundabout Rounding": ["math", "brute_force"],
    "Farmer John's Cheese Block": ["brute_force", "2d_grid"],
    "It's Mooin' Time": ["bfs", "graph"],
    "Astral Superposition": ["graph", "math"],
    "It's Mooin' Time II": ["bfs", "graph"],
    "Cow Checkups": ["sorting", "math"],
    "Reflection": ["2d_grid", "geometry"],
    "Making Mexes": ["math", "brute_force"],
    "Printing Sequences": ["brute_force", "dp"],
    "Hoof Paper Scissors Minus One": ["brute_force", "game"],
    "More Cow Photos": ["string", "brute_force"],
    "It's Mooin' Time III": ["bfs", "graph"],

    # 2026
    "Chip Exchange": ["math", "brute_force"],
    "COW Splits": ["math", "brute_force"],
}

def add_tags_to_problems(db):
    """为数据库中的所有问题添加标签"""
    for problem in db["problems"]:
        name = problem["name"]
        tags = []

        # 先检查精确匹配
        if name in EXACT_TAG_MAP:
            tags = EXACT_TAG_MAP[name].copy()
        else:
            # 使用模式匹配
            name_lower = name.lower()
            for tag, patterns in TAG_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, name_lower):
                        if tag not in tags:
                            tags.append(tag)
                        break

        # 如果没有匹配到任何标签，默认为 simulation（Bronze 级别很多都是）
        if not tags:
            tags = ["simulation", "brute_force"]

        problem["tags"] = tags

    return db

def main():
    # 读取数据库
    with open("data/usaco_bronze_db.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    # 添加标签
    db = add_tags_to_problems(db)

    # 统计标签
    tag_counts = {}
    for p in db["problems"]:
        for tag in p["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    print("标签统计:")
    for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
        print(f"  {tag}: {count}")

    # 保存
    with open("data/usaco_bronze_db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"\n数据库已更新，共 {len(db['problems'])} 道题目")

if __name__ == "__main__":
    main()