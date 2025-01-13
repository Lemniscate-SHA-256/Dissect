"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class AlgorithmVisualization {
    constructor(steps) {
        this.steps = steps;
        this.currentStep = 0;
    }
    displayCurrentStep() {
        const step = this.steps[this.currentStep];
        this.renderStep(step);
        this.highlightElements(step);
    }
    nextStep() {
        if (this.currentStep < this.steps.length - 1) {
            this.currentStep++;
            this.displayCurrentStep();
        }
    }
    previousStep() {
        if (this.currentStep > 0) {
            this.currentStep--;
            this.displayCurrentStep();
        }
    }
    renderStep(step) {
        // Implementation for rendering the current step of the algorithm
    }
    highlightElements(step) {
        // Implementation for highlighting elements based on the current step
    }
    reset() {
        this.currentStep = 0;
        this.displayCurrentStep();
    }
}
exports.default = AlgorithmVisualization;
