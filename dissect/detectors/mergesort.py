def detect_mergesort(node, code):
    has_merge = False
    has_split = False
    
    if node.type == "function_definition":
        func_name = node.child_by_field_name("name").text.decode()
        # Check for split logic (e.g., mid = len(arr)//2)
        for child in node.children:
            if child.type == "assignment" and "//2" in code[child.start_byte:child.end_byte].decode():
                has_split = True
            # Check for merge function calls
            if child.type == "call_expression" and "merge(" in code[child.start_byte:child.end_byte].decode():
                has_merge = True
    
    return {
        "is_mergesort": has_split and has_merge,
        "confidence": 0.85 if (has_split and has_merge) else 0.1
    }