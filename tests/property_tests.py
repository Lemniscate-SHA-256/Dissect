# tests/property_tests.py
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_quicksort_detection(arr):
    code = f"""
    def quicksort(arr):
        {'''...quicksort implementation...'''}
    """.encode()
    
    # Verify detector flags this as quicksort
    
    assert detect_quicksort(...)["is_quicksort"]