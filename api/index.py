from http.server import BaseHTTPRequestHandler
import urllib.parse
import json
import random

students = {f"Student{i}": random.randint(0, 100) for i in range(1, 101)}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # CORS enabled
        self.end_headers()

        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        names = query.get("name", [])
        marks = [students.get(name, None) for name in names]

        self.wfile.write(json.dumps({"marks": marks}).encode())
