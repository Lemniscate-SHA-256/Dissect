from graphviz import Digraph

class FlowVisualizer:
    def __init__(self):
        self.dot = Digraph(comment='Algorithm Flow')
        self.algorithms = []
    
    def add_algorithm(self, name, confidence):
        self.algorithms.append((name, confidence))
        self.dot.node(name, f"{name}\nConfidence: {confidence:.0%}")
    
    def render(self, filename="flowchart"):
        if not self.algorithms:
            print("No algorithms detected to visualize.")
            return
        
        # Create a central "Codebase" node
        self.dot.node("Codebase", shape="cylinder")
        
        # Connect algorithms to codebase
        for name, _ in self.algorithms:
            self.dot.edge("Codebase", name)
        
        self.dot.render(filename, cleanup=True, format='png')
        print(f"Visualization saved to {filename}.png")