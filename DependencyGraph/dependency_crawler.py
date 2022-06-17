""" 
Create Dependency crawler starting from one file using BFS
"""
import string
from node import FileNode, ClassNode, FunctionNode
from typing import Tuple

def crawl_from_file(root_file: string) -> Tuple(FileNode,ClassNode,FunctionNode):
    # do bfs from the root file
    pass

def bfs(root_file):
    # parse the file
    # create new node for file, each classes, and each functions

