#!/bin/bash
# rebuild.sh - Ensures clean build and compatible dependencies

set -e  # Exit on error

# Step 1: Clean old installations
echo "=== Cleaning old builds ==="
pip uninstall -y dissect tree-sitter || true
rm -rf build/ dist/ dissect.egg-info/
rm -rf tree-sitter-python/

# Step 2: Install correct tree-sitter version
echo "=== Installing tree-sitter 0.20.4 ==="
pip install "tree-sitter==0.20.4"

# Step 3: Rebuild parser
echo "=== Rebuilding parser ==="
git clone https://github.com/tree-sitter/tree-sitter-python
python build_languages.py

# Step 4: Reinstall dissect
echo "=== Installing dissect ==="
pip install -e .

# Step 5: Verify compatibility
echo "=== Verifying compatibility ==="
python -c "from dissect.parser import CodeParser; CodeParser()"

echo "✅ Rebuild successful! Run tests with: python -m unittest discover tests/"