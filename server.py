import http.server
import socketserver

PORT = 8890
Handler = http.server.SimpleHTTPRequestHandler

server = socketserver.TCPServer(("", PORT), Handler)
server.serve_forever()