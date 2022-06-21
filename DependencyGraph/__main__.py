# Parse Arguments
# Call Dependency Crawler

from http.server import HTTPServer,BaseHTTPRequestHandler
import view
import mermaid
import dependency_crawler

class ReqHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # create header
    self.send_response(200)
    self.end_headers()

    # create html body
    with open("graph.html","r") as f:
      html_str = f.read()
      root_node = dependency_crawler.bfs_get_file_nodes("__main__.py")
      html_str = view.replace_variables(html_str,graph=mermaid.to_mermaid(root_node))
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