# Parse Arguments
# Call Dependency Crawler


import ast
from http.server import HTTPServer,BaseHTTPRequestHandler

class ReqHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write("test".encode("utf-8"))

def run(server_class=HTTPServer, handler_class=ReqHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

# Call Create graph
# create list of dependencies for mermaid -> [[<source>,<dest>,(<source_type>,<dest_type>)],...] 
# type -> class, function, or file