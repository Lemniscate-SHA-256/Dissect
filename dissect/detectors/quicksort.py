from ast_normalizer import normalize_ast

def detect_quicksort(node, code_bytes):


    code = code_bytes.decode('utf-8', errors='ignore')
    if node.type != "function_definition":
        return {"is_quicksort": False, "confidence": 0.0}
    
    func_name = node.child_by_field_name('name').text.decode('utf-8', errors='ignore')

    # AST normalizer implementation
    normalized_ast = normalize_ast(node) # Language-agnostic AST


    # Enhanced detection metrics
    recursive_calls = 0
    partitioning = 0
    divide_and_conquer = 0
    list_operations = 0
    complexity = 0

    # Quicksort-specific checks
    def is_partition_loop(node, code_bytes):
        loop_code = code_bytes[node['start']:node['end']].decode()
        
        # Look for pivot selection patterns
        pivot_patterns = [
            r'pivot\s*=',          # Explicit pivot variable
            r'arr\[\s*0\s*\]',     # First element selection
            r'arr\[\s*-\s*1\s*\]', # Last element selection
            r'median_of_three'     # Common optimization
        ]
        
        # Look for element swapping
        swap_operations = [
            'arr[i], arr[j] = arr[j], arr[i]',  # Python
            '[arr[i], arr[j]] = [arr[j], arr[i]]',  # JS
            'swap(arr, i, j)'  # Common helper
        ]
        
        return (
            any(re.search(p, loop_code) for p in pivot_patterns) and
            any(s in loop_code for s in swap_operations)
        )
    
    # Analyze function body with context-aware checks
    for child in normalized_ast['children']:
        

        # More precise recursive call detection
        if child.type == "call_expression":
            if f"{func_name}(" in normalize_ast.split('(')[0]:
                recursive_calls += 1
        
        # Broad partitioning pattern detection
        partition_keywords = ['pivot', 'partition', 'less', 'greater', 
                             'left', 'right', 'middle', 'low', 'high']
        if any(kw in normalize_ast.lower() for kw in partition_keywords):
            partitioning += 1
        
        # List comprehension/array splitting detection
        if any(op in normalize_ast for op in ['[x for x', 'slice', 'split', '//2']):
            list_operations += 1
        
        # Enhanced divide-and-conquer detection
        if 'return' in normalize_ast and ('+' in normalize_ast or 'extend(' in normalize_ast):
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
    

    # Complexity analysis
    def estimate_complexity(node):
        depth = 0
        nested_loops = 0

        # Traverse AST to find complexity factors
        def traverse(n):
            nonlocal depth, nested_loops
            if n['type'] == 'loop_block':
                nested_loops += 1
                depth = max(depth, nested_loops)
            for c in n['children']:
                traverse(c)
            if n['type'] == ['for_statement', 'while_statement']:
                nested_loops -= 1
        
        traverse(node)

        # Complexity determination
        if depth == 1 and 'recursive' in node['operations']:
            return 'O(n log n)' # Best Case
        elif depth == 2:
            return 'O(n^2)' # Worst Case
        return 'unknown'
    


    # Confidence Calculation
    def calculate_confidence(partition, recursion, complexity):
        weights = {
            'partition': 0.5,
            'recursion': 0.3,
            'complexity': 0.2
        }
        
        score = 0
        if partition: score += weights['partition']
        if recursion: score += weights['recursion']
        
        # Complexity bonus
        if complexity == 'O(n log n)':
            score += 0.2
        elif complexity == 'O(n²)':
            score += 0.1
            
        return min(score * 1.2, 1.0)  # Allow slight overconfidence


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