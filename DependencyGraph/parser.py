import ast
from msilib.schema import Class

""" 
Parse a python file into list of classes, functions
"""

class ParsedFile():
    def __init__(self,file) -> None:
        with open(filename) as f:
            
            self.ast_tree = ast.parse()