import yaml;
import os;
import sys;
from parkinsons.components.model_train import ModelTrain;
from parkinsons.entity.config_entity import (ModelTrainConfig, ModelTrainingParams)
from exceptions.ModelBuildException import ModelBuildException;

import logging;

class ModelTrainingPipeline:
    def __init__(self):
        pass;
    def initialize_train(self):
        try:
            with open('config.yaml') as file:
                data = yaml.safe_load(file);
            with open('params.yaml') as file:
                params = yaml.safe_load(file);

            logging.info("config files open");
            model_train_confi = data['model_training'];
            model_para = params['model_train_params'];

            model_train_config: ModelTrainConfig = ModelTrainConfig(model_train_confi['data_source'], model_train_confi['model_initial_source'], model_train_confi['model_final_source'])
            model_params: ModelTrainingParams = ModelTrainingParams(model_para['learning_rate'], model_para['epochs'], model_para['batch_size']);
            logging.info("training begins");
            model_train = ModelTrain(model_train_config);
            model_train.train(model_params);
            logging.info("training ends");
        except Exception as e:
            raise ModelBuildException(e, sys);