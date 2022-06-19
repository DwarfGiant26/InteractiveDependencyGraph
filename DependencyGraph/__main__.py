# Parse Arguments
# Call Dependency Crawler


import ast

trees = ast.parse("""
import math
import numpy

class FunctionNode():
    def __init__(self,name) -> None:
        self.name = name
        self.called_functions = []
        self.line_no = 0

@something
def my_function(fname, lname):
  print(fname + " " + lname)
  print(fname)

def my_function1234123(fname, lname):
  print(fname + " " + lname)
  print(fname)
""")
from io import StringIO
from contextlib import redirect_stdout


import importlib
# implib = importlib.abc.ExecutionLoader()
for elem in trees.body:
    # if type(elem) == ast.Import:
    #     module_specs = importlib.util.find_spec(elem.names[0].name)
    #     module_path = module_specs.origin
    #     print(module_path)
    # print(ast.dump(elem))
    if type(elem) == ast.FunctionDef:
        print(elem.name)
    # exec(f"import {elem.names[0].name}")
    # f = StringIO()
    # with redirect_stdout(f):
    #     exec(f"print({elem.names[0].name}.__name__)")
    # s = f.getvalue()
    # print(s)




# Call Create graph
# create list of dependencies for mermaid -> [[<source>,<dest>,(<source_type>,<dest_type>)],...] 
# type -> class, function, or file