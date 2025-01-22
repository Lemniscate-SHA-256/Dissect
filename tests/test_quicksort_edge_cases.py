import unittest
from dissect.parser import CodeParser
from dissect.detectors.quicksort import detect_quicksort

class TestQuicksortEdgeCases(unittest.TestCase):
    def setUp(self):
        self.parser = CodeParser()
    

    def test_lomuto_partition(self):
        code = """
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr)//2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)  # Direct recursion
        """.encode('utf-8')
        
        tree = self.parser.parse(code)
        detected = any(
            detect_quicksort(node, code)["is_quicksort"]
            for node in tree.root_node.children
            if node.type == "function_definition"
        )
        self.assertTrue(detected, "List-based quicksort should be detected")

    def test_3way_partition(self):
        code = """
        def quicksort(arr):
            if len(arr) <= 1: return arr
            pivot = arr[0]
            return (
                quicksort([x for x in arr if x < pivot]) + 
                [x for x in arr if x == pivot] + 
                quicksort([x for x in arr if x > pivot])
            )
        """.encode('utf-8')
        
        tree = self.parser.parse(code)
        detected = any(
            detect_quicksort(node, code)["is_quicksort"]
            for node in tree.root_node.children
            if node.type == "function_definition"
        )
        self.assertTrue(detected, "3-way list comprehension quicksort should be detected")

        # In tests/test_quicksort_edge_cases.py
    def test_non_quicksort_recursion(self):
        code = """
        def factorial(n):
            return 1 if n <= 1 else n * factorial(n-1)
        """.encode('utf-8')
        
        tree = self.parser.parse(code)
        detected = False
        
        for node in tree.root_node.children:
            if node.type == "function_definition":
                # Pass raw bytes instead of decoded string
                result = detect_quicksort(node, code)  # <-- Remove .decode()
                if result["is_quicksort"]:
                    detected = True
        
        self.assertFalse(detected, "Non-quicksort recursion should not be detected")
    
    def test_pythonic_quicksort(self):
        code = """
        def quicksort(arr):
            return arr if len(arr) <= 1 else (
                quicksort([x for x in arr[1:] if x < arr[0]]) + 
                [arr[0]] + 
                quicksort([x for x in arr[1:] if x >= arr[0]])
            )
        """.encode()
    
    # Assert this one-liner is detected

    def test_non_recursive_quicksort(self):
        code = """
        def quicksort(arr):  # Iterative implementation
            stack = [(0, len(arr)-1)]
            while stack:
                low, high = stack.pop()
                # ... partitioning logic ...
            return arr
        """.encode()
        
        # Assert this isn't flagged as quicksort

if __name__ == "__main__":
    unittest.main()