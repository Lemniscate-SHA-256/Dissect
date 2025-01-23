def detect_quicksort(node, code_bytes):


    code = code_bytes.decode('utf-8', errors='ignore')
    if node.type != "function_definition":
        return {"is_quicksort": False, "confidence": 0.0}
    
    func_name = node.child_by_field_name('name').text.decode('utf-8', errors='ignore')
    
    # Enhanced detection metrics
    recursive_calls = 0
    partitioning = 0
    divide_and_conquer = 0
    list_operations = 0
    
    # Analyze function body with context-aware checks
    for child in node.children:
        child_code = code_bytes[child.start_byte:child.end_byte].decode(errors='ignore')
        
        # More precise recursive call detection
        if child.type == "call_expression":
            if f"{func_name}(" in child_code.split('(')[0]:
                recursive_calls += 1
        
        # Broad partitioning pattern detection
        partition_keywords = ['pivot', 'partition', 'less', 'greater', 
                             'left', 'right', 'middle', 'low', 'high']
        if any(kw in child_code.lower() for kw in partition_keywords):
            partitioning += 1
        
        # List comprehension/array splitting detection
        if any(op in child_code for op in ['[x for x', 'slice', 'split', '//2']):
            list_operations += 1
        
        # Enhanced divide-and-conquer detection
        if 'return' in child_code and ('+' in child_code or 'extend(' in child_code):
            divide_and_conquer += 1
    
    # Dynamic confidence calculation
    confidence = 0.0
    if recursive_calls >= 1:
        confidence += 0.5  # Reduced weight for recursion
    if partitioning >= 1:  # Lowered threshold
        confidence += min(0.3 * partitioning, 0.6)  # Max 0.6 for partitioning
    if divide_and_conquer >= 1:
        confidence += 0.2  # Increased weight for structure
    if list_operations >= 1:
        confidence += 0.2  # New list operations factor
    
    # Final validation check
    is_quicksort = (
        confidence >= 0.65 and  # Lowered threshold
        recursive_calls >= 1 and
        partitioning >= 1
    )
    
    return {
        "is_quicksort": is_quicksort,
        "confidence": min(confidence, 1.0)
    }