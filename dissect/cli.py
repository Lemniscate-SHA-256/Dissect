import argparse
from .parser import CodeParser
from .detectors.quicksort import detect_quicksort
from .viz import FlowVisualizer
from .detectors.bfs import detect_bfs
from .detectors.dfs import detect_dfs
from .detectors.mergesort import detect_mergesort
from .detectors.binary_search import detect_binary_search

def visualize_command(args):
    parser = CodeParser()
    tree = parser.parse_file(args.file)
    code = open(args.file, "rb").read()
    
    visualizer = FlowVisualizer()
    
    # Detect algorithms
    for node in tree.root_node.children:
        if node.type == "function_definition":
            func_name = node.child_by_field_name("name").text.decode()
            print(f"Analyzing function: {func_name}")  # Debug output
            # Detect quicksort
            qs_result = detect_quicksort(node, code)
            if qs_result["is_quicksort"]:
                visualizer.add_algorithm("Quicksort", qs_result["confidence"], "sorting")
            # Add to the detection loop:
            bfs_result = detect_bfs(node, code)
            if bfs_result["is_bfs"]:
                visualizer.add_algorithm("BFS", bfs_result["confidence"], "graph")

            dfs_result = detect_dfs(node, code)
            if dfs_result["is_dfs"]:
                visualizer.add_algorithm("DFS", dfs_result["confidence"], "graph")

            ms_result = detect_mergesort(node, code)
            if ms_result["is_mergesort"]:
                visualizer.add_algorithm("Mergesort", ms_result["confidence"], "sorting")

            bs_result = detect_binary_search(node, code)
            if bs_result["is_binary_search"]:
                visualizer.add_algorithm("Binary Search", bs_result["confidence"], "search")

    visualizer.render(args.output)

def main():
    parser = argparse.ArgumentParser(description='Dissect: Algorithm Detective')
    subparsers = parser.add_subparsers()
    
    # Visualization command
    viz_parser = subparsers.add_parser('visualize')
    viz_parser.add_argument('--file', required=True)
    viz_parser.add_argument('--output', default="flowchart")
    viz_parser.set_defaults(func=visualize_command)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()