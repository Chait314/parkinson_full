import yaml;
from parkinsons.components.model_build import Model;
from exceptions.ModelBuildException import ModelBuildException;
from parkinsons.entity.config_entity import (ModelParams, ModelConfig);
import os;
import sys;
import logging;

class ModelBuildPipeline:
    def __init__(self):
        pass;

    def initiate_pipeline(self):
        try:
            logging.info("Files opening")
            with open('config.yaml') as file:
                data = yaml.safe_load(file);
            with open('params.yaml') as file:
                params = yaml.safe_load(file);
            logging.info("Files Opened");

            model_para = params["model_params"];
            model_confi = data["model"];

            model_params: ModelParams = ModelParams(model_para["input_nodes"], model_para['hidden_layers'], model_para['output_nodes'], model_para['optimizer'], model_para['loss']);
            model_config: ModelConfig = ModelConfig(model_confi['data_source'], model_confi['model_store']);
            logging.info("Model build begins");
            model = Model(model_params, model_config);
            model.compile_model_and_store();
            logging.info("Model build Ends");
        except Exception as e:
            raise ModelBuildException(e, sys);