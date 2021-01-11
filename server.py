from handler import SimpleHTTPRequestHandlerExodo as CustomHandler

import http.server
import socketserver

PORT = 8000

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
