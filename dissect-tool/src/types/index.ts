export interface Algorithm {
    name: string;
    description: string;
    steps: VisualizationStep[];
}

export interface AnalysisResult {
    algorithms: Algorithm[];
    complexity: string;
}

export interface VisualizationStep {
    stepNumber: number;
    description: string;
    state: any; // Define the type based on the state structure you need
}