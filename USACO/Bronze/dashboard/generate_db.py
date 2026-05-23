"""
USACO Bronze 题库数据库生成脚本
自动生成包含所有题目的 JSON 数据库
"""

import json

# 所有 USACO Bronze 题目数据 (2015-2025)
# 格式: (年份-赛季, 比赛名称, Problem 1, Problem 2, Problem 3)
problems_data = [
    # ==================== 2015-16 ====================
    ("2015-16", "December", "Fence Painting", "Speeding Ticket", "Contaminated Milk"),
    ("2015-16", "January", "Promotion Counting", "Angry Cows", "Mowing the Field"),
    ("2015-16", "February", "Milk Pails", "Circular Barn", "Load Balancing"),
    ("2015-16", "US Open", "Diamond Collector", "Bull in a China Shop", "Field Reduction"),

    # ==================== 2016-17 ====================
    ("2016-17", "December", "Square Pasture", "Block Game", "The Cow-Signal"),
    ("2016-17", "January", "Don't Be Last!", "Hoof Paper Scissors", "Cow Tipping"),
    ("2016-17", "February", "Why Did the Cow Cross the Road", "Why Did the Cow Cross the Road II", "Why Did the Cow Cross the Road III"),
    ("2016-17", "US Open", "The Lost Cow", "Bovine Genomics", "Modern Art"),

    # ==================== 2017-18 ====================
    ("2017-18", "December", "Blocked Billboard", "The Bovine Shuffle", "Milk Measurement"),
    ("2017-18", "January", "Blocked Billboard II", "Lifeguards", "Out of Place"),
    ("2017-18", "February", "Teleportation", "Hoofball", "Taming the Herd"),
    ("2017-18", "US Open", "Team Tic Tac Toe", "Milking Order", "Family Tree"),

    # ==================== 2018-19 ====================
    ("2018-19", "December", "Mixing Milk", "The Bucket List", "Back and Forth"),
    ("2018-19", "January", "Shell Game", "Sleepy Cow Sorting", "Guess the Animal"),
    ("2018-19", "February", "Sleepy Cow Herding", "The Great Revegetation", "Measuring Traffic"),
    ("2018-19", "US Open", "Bucket Brigade", "Milk Factory", "Cow Evolution"),

    # ==================== 2019-20 ====================
    ("2019-20", "December", "Cow Gymnastics", "Where Am I?", "Livestock Lineup"),
    ("2019-20", "January", "Word Processor", "Photoshoot", "Race"),
    ("2019-20", "February", "Triangles", "Mad Scientist", "Swapity Swap"),
    ("2019-20", "US Open", "Social Distancing I", "Social Distancing II", "Cowntact Tracing"),

    # ==================== 2020-21 ====================
    ("2020-21", "December", "Do you know your ABCs?", "Daisy Chains", "Stuck in a Rut"),
    ("2020-21", "January", "Uddered but not Herd", "Even More Odd Photos", "Just Stalling"),
    ("2020-21", "February", "Year of the Cow", "Comfortable Cows", "Clockwise Fence"),
    ("2020-21", "US Open", "Acowdemia I", "Acowdemia II", "Acowdemia III"),

    # ==================== 2021-22 ====================
    ("2021-22", "December", "Lonely Photo", "Air Cowditioning", "Walking Home"),
    ("2021-22", "January", "Herdle", "Non-Transitive Dice", "Drought"),
    ("2021-22", "February", "Sleeping in Class", "Photoshoot 2", "Blocks"),
    ("2021-22", "US Open", "Photoshoot", "Counting Liars", "Alchemy"),

    # ==================== 2022-23 ====================
    ("2022-23", "December", "Cow College", "Feeding the Cows", "Reverse Engineering"),
    ("2022-23", "January", "Leaders", "Air Cowditioning II", "Moo Operations"),
    ("2022-23", "February", "Hungry Cow", "Stamp Grid", "Watching Mooloo"),
    ("2022-23", "US Open", "FEB", "Moo Language", "Rotate and Shift"),

    # ==================== 2023-24 ====================
    ("2023-24", "December", "Candy Cane Feast", "Cowntact Tracing 2", "Farmer John Actually Farms"),
    ("2023-24", "January", "Majority Opinion", "Cannon Ball", "Balancing Bacteria"),
    ("2023-24", "February", "Palindrome Game", "Milk Exchange", "Maximizing Productivity"),
    ("2023-24", "US Open", "Logical Moos", "Walking Along a Fence", "Farmer John's Favorite Permutation"),

    # ==================== 2024-25 ====================
    ("2024-25", "December", "Roundabout Rounding", "Farmer John's Cheese Block", "It's Mooin' Time"),
    ("2024-25", "January", "Astral Superposition", "It's Mooin' Time II", "Cow Checkups"),
    ("2024-25", "February", "Reflection", "Making Mexes", "Printing Sequences"),
    ("2024-25", "US Open", "Hoof Paper Scissors Minus One", "More Cow Photos", "It's Mooin' Time III"),

    # ==================== 2026 ====================
    ("2026", "First", "Chip Exchange", "COW Splits", "Photoshoot"),
    ("2026", "Second", "TBA", "TBA", "TBA"),
    ("2026", "Third", "TBA", "TBA", "TBA"),
]

# 已知的 cpids (从用户现有的 py 文件中获取)
known_cpids = {
    "Speeding Ticket": 568,
    "Milk Pails": 615,
    "Diamond Collector": 639,
    "The Cow-Signal": 665,
    "Cow Tipping": 689,
    "Cross Roads": 711,  # Why Did the Cow Cross the Road
    "Bovine Genomics": 736,
    "Out of Place": 785,
    "Shell Game": 891,
    "Measuring Traffic": 917,
    "Cow Gymnastics": 963,
    "Triangles": 1011,
    "Mad Scientist": 1012,
    "Daisy Chains": 1060,
    "Even More Odd Photos": 1084,
    "Cow College": 1251,
    "Hungry Cow": 1299,
    "Roundabout Rounding": 1443,
    "Reflection": 1491,
}

def generate_slug(name):
    """将题目名称转换为 URL slug 格式"""
    # 移除撇号和特殊字符
    name = name.replace("'", "").replace("?", "").replace("!", "")
    # 转换为小写并用下划线连接
    parts = name.lower().split()
    return "_".join(parts)

def create_problem_entry(year_season, contest, problem_name, problem_num, cpid=None):
    """创建单个题目条目"""
    # 确定年份和赛季
    if "-" in year_season:
        year_part, season_part = year_season.split("-")
        year = year_part
        contest_season = season_part
    else:
        year = year_season
        contest_season = contest

    contest_id_map = {
        "December": "dec",
        "January": "jan",
        "February": "feb",
        "US Open": "open",
        "First": "first",
        "Second": "second",
        "Third": "third"
    }

    slug = generate_slug(problem_name)
    usaco_url = f"https://usaco.org/index.php?page=viewproblem2&cpid={cpid}" if cpid else None

    return {
        "year": int(year),
        "year_season": year_season,
        "contest": contest,
        "contest_id": contest_id_map.get(contest, contest.lower()),
        "problem_num": problem_num,
        "name": problem_name,
        "slug": slug,
        "cpid": cpid,
        "usaco_url": usaco_url,
        "local_file": None,  # 后续如果有本地文件则填充
        "tags": [],  # 待填充
        "difficulty": None,  # 待填充 (1-5)
        "notes": None
    }

def generate_database():
    """生成完整的数据库"""
    problems = []

    for year_season, contest, p1, p2, p3 in problems_data:
        problems.append(create_problem_entry(year_season, contest, p1, 1))
        problems.append(create_problem_entry(year_season, contest, p2, 2))
        problems.append(create_problem_entry(year_season, contest, p3, 3))

    # 按年份和比赛排序
    problems.sort(key=lambda x: (x["year"], x["contest_id"], x["problem_num"]))

    # 填充已知的 cpid
    for p in problems:
        for name, cpid in known_cpids.items():
            if name.lower() in p["name"].lower() or p["name"].lower() in name.lower():
                if p["cpid"] is None:
                    p["cpid"] = cpid
                    p["usaco_url"] = f"https://usaco.org/index.php?page=viewproblem2&cpid={cpid}"

    return problems

if __name__ == "__main__":
    problems = generate_database()

    # 读取现有的 metadata
    with open("data/usaco_bronze_db.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    db["problems"] = problems
    db["metadata"]["total_problems"] = len(problems)

    # 保存
    with open("data/usaco_bronze_db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"数据库已更新，共 {len(problems)} 道题目")
    print("\n按年份统计:")
    year_counts = {}
    for p in problems:
        year_counts[p["year"]] = year_counts.get(p["year"], 0) + 1
    for year in sorted(year_counts.keys()):
        print(f"  {year}: {year_counts[year]} 道")