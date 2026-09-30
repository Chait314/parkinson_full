from parkinsons.components.model_eval import ModelEvaluate
from parkinsons.entity.config_entity import ModelEvalConfig
import yaml;
import os;
import sys;
import keras;
from exceptions.ModelEvaluationException import ModelEvaluationException;
import logging;

class ModelEvalPipeline:
    def __init__(self):
        pass;
    def evaluate_pipeline(self):
        try:
            with open('config.yaml', 'r') as file:
                data = yaml.safe_load(file);
            model_eval_confi = data['model_evaluation'];
            logging.info("It is being Evaluated");
            model_evaluation_config: ModelEvalConfig = ModelEvalConfig(model_eval_confi['data_source'], model_eval_confi['model_source'], os.environ['MLFLOW_TRACKING_URI']);
            model_evaluation = ModelEvaluate(model_evaluation_config);
            model_evaluation.evaluate();
            logging.info("Eval done");
        except Exception as e:
            raise ModelEvaluationException(e, sys);