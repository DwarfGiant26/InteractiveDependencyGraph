# Parse Arguments
# Call Dependency Crawler


import ast

print(ast.dump(ast.parse("""
import math
import numpy

@something
def my_function(fname, lname):
  print(fname + " " + lname)
  print(fname)
""")))


# Call Create graph
# create list of dependencies for mermaid -> [[<source>,<dest>,(<source_type>,<dest_type>)],...] 
# type -> class, function, or file