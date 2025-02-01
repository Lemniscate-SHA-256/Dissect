
Objective  Success Metrics  Timeline

Accurate Detection	<5% false positive/negative   rate	MVP

Multi-Language Support	Python, JavaScript, Java	v1.2

Educational UX	Netron-like interactive visualization	v1.5

Enterprise Adoption	Integration with VSCode/IntelliJ	v2.0


Features
ML Algorithm Detection
Personal Model based on Dissect app
Algorithm tester
Runtime Analysis Mode
Ast Visualizer like from debug visualizer


Roadmap & Milestones
Phase 1: Core Detection (0-6 months)
Quicksort detection

BFS/DFS detection

Complexity analysis
Phase 2: Ecosystem (6-12 months)
VSCode extension

REST API for CI integration
Phase 3: Intelligence (12-18 months)
Auto-suggest optimizations ("Use mergesort here?")

Code transformation ("Convert to Hoare partition")

 Visualization Strategy
Design Principles
Netron Inspiration:

Zoomable algorithm flow graphs

Layer toggles (complexity, variants)

Interactive Elements:

Click nodes → Show code snippets

Hover → Complexity analysis (O(n))

Export Formats: PNG, SVG, PDF, LaTeX

Tech Stack
Core: Graphviz → DOT → PNG/SVG

Web UI: D3.js + WebComponents (future)


Algorithm Detection Framework
AST Parsing (Tree-sitter)
Pattern Matching
Confidence Aggregation



23 01 25
- Universal AST Normalizer for quicksort detector
    - ast_normalizer.py
        - extract_identifier()
        - detect_operations()
        - normalize_ast()
(Done)

25 01 25
- Universal AST Normalizer integration for quicksort detector
    - Function Declaration
    - Function embedding in recursive call detection
    - Function embedding in broad partition detection
    - Function embedding in comprehension/array splitting detection
    - Function embedding in divide-and-conquer detection
(Done)

27 01 05
- Add Quicksort Specific Checks
    - Pivot Selection Patterns
    - Element Swapping Patterns
- Complexity analysis add for quicksort detector
(Done)
- Implementation of Confidence Calculation for robust detection
(Done)
=
-Add Test Cases for Quicksort
(Done)


01 02 25
- Units tests were added, and the quicksort test was updated to use unittests instead
- Added "import re" Statements for quicksort.py & ast_normalizer.py
- Added Error Handling for the AST normalizer
- What is re? (Answered)
- Reading unittest documentation (5%)
(Done)

- Test Quicksort

- CI/CD Pipeline integration
    - Automatic algorithm complexity checks
    prevention of performance anti-patterns
    - Documentation generation on merge

- Comprehensive Test Structure
- Detectors parts for quicksort : AST analysis for naming patterns and explicit recursion and Unique property analysis (Eg, quicksort, partition loop)
- Confidence calculation complexity bonus add
- test update
- Adversarial code upgrade for quicksort