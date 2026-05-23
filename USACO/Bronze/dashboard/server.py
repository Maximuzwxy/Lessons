"""
USACO Bronze 题库 Web 服务器
提供 JSON API 和前端页面
"""

import json
import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

PORT = 8080
DB_PATH = os.path.join(os.path.dirname(__file__), "data", "usaco_bronze_db.json")
WEB_DIR = os.path.join(os.path.dirname(__file__), "web")

def get_local_ip():
    """获取本机局域网 IP 地址"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class USACOHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/problems":
            self.send_json_api()
        elif path == "/api/tags":
            self.send_tags_api()
        elif path == "/" or path == "/index.html":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()

    def send_json_api(self):
        try:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                db = json.load(f)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(json.dumps(db, ensure_ascii=False).encode("utf-8"))
        except Exception as e:
            self.send_error(500, f"Error loading database: {e}")

    def send_tags_api(self):
        try:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                db = json.load(f)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(db["metadata"]["tags"], ensure_ascii=False).encode("utf-8"))
        except Exception as e:
            self.send_error(500, f"Error loading tags: {e}")

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    local_ip = get_local_ip()

    # 绑定到所有网络接口
    server_address = ("0.0.0.0", PORT)
    server = HTTPServer(server_address, USACOHandler)

    print("=" * 50)
    print("USACO Bronze 题库服务器")
    print("=" * 50)
    print(f"本地访问:   http://localhost:{PORT}")
    print(f"局域网访问: http://{local_ip}:{PORT}")
    print(f"API 接口:   http://{local_ip}:{PORT}/api/problems")
    print("=" * 50)
    print("按 Ctrl+C 停止服务器")
    print("=" * 50)

    server.serve_forever()

if __name__ == "__main__":
    main()