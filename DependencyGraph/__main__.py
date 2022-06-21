# Parse Arguments
# Call Dependency Crawler


import ast
from http.server import HTTPServer,BaseHTTPRequestHandler
import view

class ReqHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # create header
    self.send_response(200)
    self.end_headers()

    # create html body
    with open("graph.html","r") as f:
      html_str = f.read()
      html_str = view.replace_variables(html_str,)
      self.wfile.write(html_str.encode("utf-8"))

def run(port, address, server_class=HTTPServer, handler_class=ReqHandler):
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

PORT = 8000
ADDRESS = 'localhost'

print(f"To view graph, go to http://localhost:8000")
run(PORT,ADDRESS)

# Call Create graph
# create list of dependencies for mermaid -> [[<source>,<dest>,(<source_type>,<dest_type>)],...] 
# type -> class, function, or file