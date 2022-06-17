# Parse Arguments
# Call Dependency Crawler
# Call Create graph

import ast

print(ast.dump(ast.parse("""
@something
def my_function(fname, lname):
  print(fname + " " + lname)
  print(fname)
"""), indent=4))