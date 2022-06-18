import ast
import importlib

class FileNode():
    def __init__(self,name) -> None:
        self.name = name
        self.imported_filenames = []
        self.classes = []
        self.functions = []
        self.dependency_file_nodes = []

        # get script
        with open(name) as f:
            self.script = f.read()
            self.ast_tree = ast.parse(self.script)

        # get imports, functions, and classes
        for elem in self.ast_tree.body:
            if type(elem) == ast.Import:
                # get module path
                import_name = elem.names[0].name
                module_specs = importlib.util.find_spec(import_name)
                module_path = module_specs.origin
                # create node for imported file
                child_file_node = FileNode(module_path)
                self.dependency_file_nodes.append(child_file_node)
            if type(elem) == ast.ClassDef:
                class_name = elem.name
                self.classes.append(class_name)
            if type(elem) == ast.FunctionDef:
                function_name = elem.name
                self.functions.append(function_name)
        

class ClassNode():
    def __init__(self,name) -> None:
        self.name = name
        self.imported_classes = []
        self.line_no = 0
        self.functions = []
        self.inner_classes = []

class FunctionNode():
    def __init__(self,name) -> None:
        self.name = name
        self.called_functions = []
        self.line_no = 0