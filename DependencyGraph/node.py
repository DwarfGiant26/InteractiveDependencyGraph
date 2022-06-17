class FileNode():
    def __init__(self,name) -> None:
        self.name = name
        self.imported_files = []
        self.script = ""
        self.classes = []
        self.functions = []

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