""" 
Create Dependency crawler starting from one file using BFS
"""
import string
from node import FileNode, ClassNode, FunctionNode
from typing import Tuple

# def crawl_from_file(root_file_name: string) -> Tuple(FileNode,ClassNode,FunctionNode):
#     # do bfs from the root file
#     pass

def bfs_get_file_nodes(root_file_name):
    fringes = []
    
    # initialize root node
    root_node = FileNode(root_file_name)
    root_node.get_list_imports()
    fringes.extend(root_node.dependency_file_nodes)

    # bfs through the rest of the files
    for file_node in fringes:
        file_node.get_list_imports()
        fringes.extend(file_node.dependency_file_nodes)

    return root_node
