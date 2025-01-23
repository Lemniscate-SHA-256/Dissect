from dissect.parser import CodeParser
import unittest

class TestParser(unittest.TestCase):
    def test_python_parsing(self):
        parser = CodeParser()
        tree = parser.parse_file("tests/test_quicksort.py", language='python')
        self.assertEqual(tree.root_node.type, 'module')

    def test_javascript_parsing(self):
        parser = CodeParser()
        code = """
        function test() {
            console.log("JS parsing works");
        }
        """.encode()
        
        # Parse with explicit language specification
        tree = parser.parse(code, language='javascript')
        self.assertEqual(tree.root_node.type, 'program')