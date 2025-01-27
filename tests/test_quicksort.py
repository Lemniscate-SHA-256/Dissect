# tests/test_quicksort.py
TEST_CASES = [
    {
        "code": """
        def quicksort(arr):
            if len(arr) <= 1: return arr
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)
        """,
        "expected": True,
        "complexity": "O(n log n)"
    },
    {
        "code": """
        def fake_sort(arr):  # Looks like quicksort but isn't
            if len(arr) < 2: return arr
            mid = arr[len(arr)//2]
            left = [x for x in arr if x < mid]
            right = [x for x in arr if x > mid]
            return fake_sort(left) + [mid] + fake_sort(right)
        """,
        "expected": False
    }
]