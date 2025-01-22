# Dissect - Algorithm Detective 🔍

[![CI/CD](https://github.com/yourusername/dissect/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/dissect/actions)
[![Coverage](https://codecov.io/gh/yourusername/dissect/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/dissect)

**Automatically detect, analyze, and visualize algorithms in codebases**

---

## Overview
Dissect scans your code to:
- 🔎 **Identify algorithms** (sorting, graph traversal, etc.)
- 📊 **Analyze complexity** (time/space Big-O notation)
- 🎨 **Generate visualizations** (Netron-like flowcharts)

![flowchart](https://github.com/user-attachments/assets/310a4051-c8f9-4d20-bbbc-0916de4faa8a)


## Features
- **Multi-Language Support**: Python, JavaScript, Java (more coming)
- **Algorithm Taxonomy**: Categorizes implementations into hierarchies
- **Educational Annotations**: Explains algorithm logic in context
- **CI/CD Ready**: Integrates with GitHub Actions

## Installation
```bash
pip install dissect
```

## Usage
**Basic Detection**:
```bash
dissect analyze --file ./src/sorting.py

# Output:
# [✓] quicksort (sorting) - Confidence: 92%
# [✓] bfs (graph) - Confidence: 85%
```

**Visualization**:
```bash
dissect visualize --file ./src/graph.py --output architecture
# Saves architecture.png
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit changes (`git commit -m 'feat: add amazing feature'`)
4. Push to branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License
Distributed under the MIT License. See `LICENSE` for more information.

---
**Dissect** - Because great code deserves to be understood. 🧠
