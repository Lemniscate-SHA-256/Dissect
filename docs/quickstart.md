# Dissect Quickstart

## Basic Usage
```bash
# Detect algorithms in a file
dissect analyze --file my_code.py

# Generate visualization
dissect visualize --file my_code.py --output flowchart
```

## Supported Algorithms
| Algorithm       | Detection Scope          |
|-----------------|--------------------------|
| Quicksort       | Lomuto/Hoare variants    |
| BFS             | Queue-based traversal    |
| DFS             | Stack/recursive variants |
| Binary Search   | Iterative/recursive      |