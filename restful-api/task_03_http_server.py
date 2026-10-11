
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(
                b"Hello, this is a simple API!"
            )

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            response = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header(
                "Content-Type", "application/json; charset=utf-8"
            )
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)

        elif self.path == "/status":
            response = b"OK"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(response)

        else:
            response = b"Endpoint not found"

            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(response)


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, APIHandler)

    print("Server running on port 8000...")
    httpd.serve_forever()
