""" 
Create Dependency crawler starting from one file using BFS
"""
import string
from node import FileNode, ClassNode, FunctionNode
from typing import Tuple

def crawl_from_file(root_file_name: string) -> Tuple(FileNode,ClassNode,FunctionNode):
    # do bfs from the root file
    pass

def bfs(root_file_name):
    # parse the file
    # create new node for file, each classes, and each functions
    root_file_node = FileNode(root_file_name)
    fringes = [root_file_name]
    for file in fringes:
        # get list of imported files
        # get list of classes
        # get list of functions
        for cls in classes:
            # get list of functions in this class
