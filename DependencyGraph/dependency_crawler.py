""" 
Create Dependency crawler starting from one file using BFS
"""
import string
from node import FileNode, ClassNode, FunctionNode
from typing import Tuple

def crawl_from_file(root_file_name: string) -> Tuple(FileNode,ClassNode,FunctionNode):
    # do bfs from the root file
    pass

def bfs_get_file_nodes(root_file_name):
    fringes = [root_file_name]
    for filename in fringes:
        file_node = FileNode(filename)
        fringes.extend(file_node.dependency_file_nodes)

def get_
