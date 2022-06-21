def to_mermaid(file_root_node):
    # bfs
    # for every node A create  B[alias] --> A[alias] where B is all the imported files
    graph_str = ""

    fringes = [file_root_node]
    for file_node in fringes:
        for imported_node in file_node.dependency_file_nodes:
            graph_str += f"{imported_node.name} --> {file_node.name}\n"    
        fringes.extend(file_node.dependency_file_nodes)
    
    
    return graph_str