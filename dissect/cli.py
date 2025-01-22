import argparse
from .parser import CodeParser
from .detectors.quicksort import detect_quicksort
from .viz import FlowVisualizer

def visualize_command(args):
    parser = CodeParser()
    tree = parser.parse_file(args.file)
    code = open(args.file, "rb").read()
    
    visualizer = FlowVisualizer()
    
    # Detect algorithms
    for node in tree.root_node.children:
        if node.type == "function_definition":
            # Detect quicksort
            qs_result = detect_quicksort(node, code)
            if qs_result["is_quicksort"]:
                visualizer.add_algorithm("Quicksort", qs_result["confidence"])
            
            # Add other detectors here (BFS/DFS etc)
    
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