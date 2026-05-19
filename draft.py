# from openai import OpenAI
#
# client = OpenAI(
#     api_key="sk-MjjdO3XztzQ392cWhw4JkgPNdCCOBtP8cQIZhtvD2w8qPwxS",
#     base_url="https://api.moonshot.cn/v1"  # 注意：去掉末尾空格！
# )
#
# response = client.chat.completions.create(
#     model="kimi-k2.5",
#     messages=[{"role": "user", "content": "你好"}]
# )
# print(response.choices[0].message.content)


# from openai import OpenAI
#
# client = OpenAI(
#     api_key="sk-kimi-BcjGM2ArS81YwgAhl4Hzs9etylj6p3aujHk61jHO3qnn8CtSkhBDtkemlo4SDcNo",
#     base_url="https://api.moonshot.cn/v1"  # ✅ 去掉末尾空格
# )
#
# response = client.chat.completions.create(
#     model="kimi-code",
#     messages=[{"role": "user", "content": "你好"}]
# )
# print(response.choices[0].message.content)


# !/usr/bin/env python3
"""
Kimi Code 直接调用 - 伪装成 Coding Agent
"""

import requests
import json

API_KEY = "sk-kimi-BcjGM2ArS81YwgAhl4Hzs9etylj6p3aujHk61jHO3qnn8CtSkhBDtkemlo4SDcNo"
BASE_URL = "https://api.kimi.com/coding/v1"

# 关键：模拟 Roo Code 的请求头
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "RooCode/3.2.0",
    "X-Vendor-Name": "RooCode",
    "Accept": "application/json"
}


def chat(message):
    data = {
        "model": "kimi-for-coding",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 1000
    }

    response = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=data,
        timeout=60
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"请求失败: {response.status_code} - {response.text}")


# 使用示例
if __name__ == "__main__":
    try:
        result = chat("你好，请介绍自己")
        print(result)
    except Exception as e:
        print(f"错误: {e}")