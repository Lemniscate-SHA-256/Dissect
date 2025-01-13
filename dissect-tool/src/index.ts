class App {
    constructor() {
        this.analyzer = new Analyzer();
        this.visualization = new AlgorithmVisualization();
    }

    start() {
        // Initialize server and middleware
        this.setupRoutes();
        // Start the server
    }

    setupRoutes() {
        const routes = setRoutes(this.visualization);
        // Use routes in the application
    }
}

const app = new App();
app.start();

export default app;