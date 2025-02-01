import unittest
from dissect.parser import CodeParser
from dissect.detectors.quicksort import detect_quicksort

class TestQuicksortDetection(unittest.TestCase):
    def setUp(self):
        self.parser = CodeParser()
        
    def _analyze_code(self, code):
        encoded_code = code.encode('utf-8')
        tree = self.parser.parse(encoded_code)
        for node in tree.root_node.children:
            if node.type == "function_definition":
                return detect_quicksort(node, encoded_code)
        return None

    def test_standard_quicksort(self):
        code = """
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)
        """
        result = self._analyze_code(code)
        self.assertIsNotNone(result)
        self.assertTrue(result["is_quicksort"])
        self.assertGreaterEqual(result["confidence"], 0.7)
        print(f"Standard Quicksort: {result}")

    def test_inplace_quicksort(self):
        code = """
        def quicksort(arr, low, high):
            if low < high:
                pivot = partition(arr, low, high)
                quicksort(arr, low, pivot - 1)
                quicksort(arr, pivot + 1, high)
        """
        result = self._analyze_code(code)
        self.assertTrue(result["is_quicksort"])
        print(f"In-place Quicksort: {result}")

    def test_not_quicksort(self):
        code = """
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)
        """
        result = self._analyze_code(code)
        self.assertFalse(result["is_quicksort"])
        print(f"Non-Quicksort (Mergesort): {result}")

    def test_edge_case_empty(self):
        code = """
        def empty_sort(arr):
            return arr
        """
        result = self._analyze_code(code)
        self.assertFalse(result["is_quicksort"])
        print(f"Edge Case (Empty): {result}")

if __name__ == "__main__":
    unittest.main(verbosity=2)