from tree_sitter import Language, Parser
import os

class CodeParser:
    def __init__(self):
        # Load parser from absolute path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        so_path = os.path.join(current_dir, '..', 'build', 'python.so')
        self.language = Language(so_path, 'python')
        self.parser = Parser()
        self.parser.set_language(self.language)
    
    def parse_file(self, file_path: str):
        """Parse a file and return its AST"""
        with open(file_path, "rb") as f:
            code = f.read()
        return self.parser.parse(code)