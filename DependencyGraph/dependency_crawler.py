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
    fringes = []
    
    # initialize root node
    root_node = FileNode(filename)
    fringes.extend(root_node.dependency_file_nodes)

    # bfs through the rest of the files
    for filename in fringes:
        file_node = FileNode(filename)
        fringes.extend(file_node.dependency_file_nodes)

    return root_node
