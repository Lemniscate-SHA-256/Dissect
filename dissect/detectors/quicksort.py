def detect_quicksort(node, code_bytes):
    code = code_bytes.decode('utf-8')
    if node.type != "function_definition":
        return {"is_quicksort": False, "confidence": 0.0}
    
    func_name = node.child_by_field_name('name').text.decode('utf-8')
    
    # Detection metrics
    recursive_calls = 0
    partitioning = 0
    divide_and_conquer = 0
    
    # Analyze function body
    for child in node.children:
        child_code = code_bytes[child.start_byte:child.end_byte].decode()
        
        # Recursive calls (any number)
        if f"{func_name}(" in child_code:
            recursive_calls += 1
        
        # Partitioning patterns
        if any(keyword in child_code.lower() for keyword in ['pivot', 'partition', 'less', 'greater']):
            partitioning += 1
        
        # Divide-and-conquer structure
        if 'return' in child_code and '+' in child_code:
            divide_and_conquer += 1
    
    # Confidence calculation
    confidence = 0.0
    if recursive_calls >= 1:  # Relaxed from 2
        confidence += 0.6
    if partitioning >= 2:
        confidence += 0.3
    if divide_and_conquer >= 1:
        confidence += 0.1
    
    return {
        "is_quicksort": confidence >= 0.7,
        "confidence": confidence
    }