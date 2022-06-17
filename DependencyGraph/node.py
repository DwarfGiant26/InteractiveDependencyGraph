class FileNode():
    def __init__(self) -> None:
        self.name = ""
        self.imported_files = []
        self.script = ""
        self.classes = []

class ClassNode():
    def __init__(self) -> None:
        self.name = ""
        self.imported_classes = []
        self.script = ""
        self.functions = []

class FunctionNode():
    def __init__(self) -> None:
        self.name = ""
        self.called_functions = []
        self.script = ""