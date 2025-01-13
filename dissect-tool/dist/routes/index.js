"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.setRoutes = void 0;
const express_1 = require("express");
const index_1 = __importDefault(require("../controllers/index"));
const router = (0, express_1.Router)();
const indexController = new index_1.default();
function setRoutes(app) {
    app.use('/visualize', router);
    router.get('/', indexController.startVisualization.bind(indexController));
    router.post('/step', indexController.controlStep.bind(indexController));
}
exports.setRoutes = setRoutes;
