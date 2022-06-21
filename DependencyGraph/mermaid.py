def to_mermaid(file_root_node):
    # bfs
    # for every node A create  B[alias] --> A[alias] where B is all the imported files
    graph_str = ""

    fringes = [file_root_node]
    for file_node in fringes:
        for imported_node in file_node.dependency_file_nodes:
            # dependency between files
            graph_str += f"{imported_node.name} --> {file_node.name}\n"    
            
            # classes and functions inside
            graph_str += f"subgraph {file_node.name}\n"
            # classes
            for cls in file_node.classes:
                graph_str += f"Class:{cls}\n"
            # functions
            for fun in file_node.functions:
                graph_str += f"Function:{fun}\n"
            graph_str += "end\n"

        fringes.extend(file_node.dependency_file_nodes)
    
    
    return graph_str