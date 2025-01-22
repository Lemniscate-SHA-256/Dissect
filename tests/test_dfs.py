import unittest
from dissect.parser import CodeParser
from dissect.detectors.dfs import detect_dfs

class TestDFSDetection(unittest.TestCase):
    def setUp(self):
        self.parser = CodeParser()
    
    def test_iterative_dfs(self):
        code = """
        def dfs(root):
            stack = [root]
            visited = set()
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(reversed(node.children))
            return visited
        """.encode()
        
        tree = self.parser.parse(code)
        detected = any(
            detect_dfs(node, code)["is_dfs"]
            for node in tree.root_node.children
            if node.type == "function_definition"
        )
        self.assertTrue(detected, "Iterative DFS should be detected")
    
    def test_recursive_dfs(self):
        code = """
        def dfs(node, visited=None):
            if visited is None:
                visited = set()
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            return visited
        """.encode()
        
        tree = self.parser.parse(code)
        detected = any(
            detect_dfs(node, code)["is_dfs"]
            for node in tree.root_node.children
            if node.type == "function_definition"
        )
        self.assertTrue(detected, "Recursive DFS should be detected")

if __name__ == "__main__":
    unittest.main()