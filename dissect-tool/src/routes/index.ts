import { Router } from 'express';
import IndexController from '../controllers/index';

const router = Router();
const indexController = new IndexController();

export function setRoutes(app) {
    app.use('/visualize', router);
    router.get('/', indexController.startVisualization.bind(indexController));
    router.post('/step', indexController.controlStep.bind(indexController));
}