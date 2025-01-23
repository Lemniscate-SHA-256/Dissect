import unittest
from dissect.parser import CodeParser
from dissect.detectors.mergesort import detect_mergesort

class TestMergesortDetection(unittest.TestCase):
    def setUp(self):
        self.parser = CodeParser()
    
    def test_standard_mergesort(self):
        code = """
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)
        """.encode()
        
        tree = self.parser.parse(code)
        detected = False
        for node in tree.root_node.children:
            if node.type == "function_definition":
                result = detect_mergesort(node, code)
                if result["is_mergesort"]:
                    detected = True
                    self.assertGreaterEqual(result["confidence"], 0.8)
        self.assertTrue(detected)

    def test_3way_mergesort(self):
        code = """
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            m1 = len(arr) // 3
            m2 = 2 * m1
            return merge3(
                mergesort(arr[:m1]),
                mergesort(arr[m1:m2]),
                mergesort(arr[m2:])
            )
        """.encode()
        
        tree = self.parser.parse(code)
        detected = any(
            detect_mergesort(node, code)["is_mergesort"]
            for node in tree.root_node.children
            if node.type == "function_definition"
        )
        self.assertTrue(detected)

    def test_negative_case(self):
        code = """
        def quicksort(arr):
            return arr  # Not a mergesort
        """.encode()
        
        tree = self.parser.parse(code)
        detected = any(
            detect_mergesort(node, code)["is_mergesort"]
            for node in tree.root_node.children
            if node.type == "function_definition"
        )
        self.assertFalse(detected)

if __name__ == "__main__":
    unittest.main()