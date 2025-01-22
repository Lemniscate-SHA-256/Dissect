import unittest
from dissect.parser import CodeParser
from dissect.detectors.quicksort import detect_quicksort

class TestQuicksortDetection(unittest.TestCase):
    def setUp(self):
        self.parser = CodeParser()
        self.sample_code = """
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)
        """
        self.tree = self.parser.parse(self.sample_code)
    
    def test_positive_case(self):
        for node in self.tree.root_node.children:
            if node.type == "function_definition":
                result = detect_quicksort(node, self.sample_code)
                self.assertTrue(result["is_quicksort"])
                self.assertGreaterEqual(result["confidence"], 0.8)
    
    def test_negative_case(self):
        non_qs_code = "def bubble_sort(arr): ..."
        tree = self.parser.parse(non_qs_code)
        for node in tree.root_node.children:
            result = detect_quicksort(node, non_qs_code)
            self.assertFalse(result["is_quicksort"])

if __name__ == "__main__":
    unittest.main()