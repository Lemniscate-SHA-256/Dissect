# tests/test_parser.py
from dissect.parser import CodeParser

def test_parser():
    parser = CodeParser()
    tree = parser.parse_file("test_quicksort.py")
    assert tree.root_node.type == 'module'  # Basic AST check